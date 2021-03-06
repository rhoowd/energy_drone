#!/usr/bin/env python
#coding=utf8
"""
====================================
 :mod:`main` Main
====================================
.. moduleauthor:: Daewoo Kim
.. note:: note...

설명
=====

This is for analyzing energy consumption of drone,
and propose the neural network model for drone's energy consumption

참고
====
 * https://github.com/rhoowd/energy_drone

관련 작업자
===========

본 모듈은 다음과 같은 사람들이 관여했습니다:
 * Daewoo Kim
 * Se-eun Yoon

 CUDA_VISIBLE_DEVICES=0

"""
import config
import extract_data as ed
import log_result as log
import models
import graph
from sklearn.model_selection import train_test_split


FLAGS = config.flags.FLAGS


if __name__ == '__main__':

    # Load data from file
    if FLAGS.d_t == "s":
        xy = ed.extract_data_speed(n_history=FLAGS.n_h, n_sample=FLAGS.n_s, filename=FLAGS.f_n)
    elif FLAGS.d_t == "v":
        xy = ed.extract_data_velocity(n_history=FLAGS.n_h, n_sample=FLAGS.n_s, filename=FLAGS.f_n)
    else:
        print "Wrong data type"
        exit()
    x_data = xy[:, 0:-1]
    y_data = xy[:, [-1]]
    log.logger.info("x_shape: " + str(x_data.shape) + ", y_shape:" + str(y_data.shape))

    # Split data for test
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=FLAGS.test_size,
                                                        random_state=FLAGS.seed)

    # Create model
    model = models.flexible_model(input_dim=x_data.shape[1], output_dim=y_data.shape[1])

    # Start training
    model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=FLAGS.n_e,
              batch_size=FLAGS.b_s, verbose=FLAGS.verbose)

    # Evaluate the model
    scores = model.evaluate(x_test, y_test)
    log.logger.info("ACC(test):\t" + str(scores[2] * 100) + "%\t" + log.filename + " s" + str(FLAGS.seed) + "\t")
    log.logger.info("MSE(test):\t" + str(scores[1]) + "\t" + log.filename + " s"+ str(FLAGS.seed) + "\t")
    scores = model.evaluate(x_data, y_data)
    log.logger.info("ACC(all):\t" + str(scores[2] * 100) + "%\t" + log.filename + " s" + str(FLAGS.seed) + "\t")
    log.logger.info("MSE(all):\t" + str(scores[1]) + "\t" + log.filename + " s" + str(FLAGS.seed) + "\t")

    # Save model
    model_json = model.to_json()
    with open("result/model/"+log.filename+".json", "w") as json_file:
        json_file.write(model_json)  # serialize model to JSON
    model.save_weights("result/model/"+log.filename+".h5")  # weight
    print("Save model ... done")

    # Make graph
    if FLAGS.graph == 1:
        est = model.predict(x_data)
        graph.draw_graph(x_data[:, -1], y_data, est)
        print("Save graph ... done")
