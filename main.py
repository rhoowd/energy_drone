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

"""
import config
import extract_data as ed
import log_result

from keras.models import Sequential
from keras.layers import Dense


FLAGS = config.flags.FLAGS

if __name__ == '__main__':

    n_s = FLAGS.n_s
    n_h = FLAGS.n_h

    xy = ed.extract_data_speed(n_history=n_h, n_sample=n_s, filename=FLAGS.f_n)

    x_data = xy[:, 0:-1]
    y_data = xy[:, [-1]]

    log_result.logger.info("hello")
    print "x_shape:", x_data.shape, "; y_shape:", y_data.shape

    # create model
    model = Sequential()
    model.add(Dense(12, input_dim=FLAGS.n_h, init='uniform', activation='relu'))
    model.add(Dense(15, init='uniform', activation='relu'))
    model.add(Dense(15, init='uniform', activation='relu'))
    model.add(Dense(1, init='uniform', activation='relu'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_squared_error'])

    model.fit(x_data, y_data, nb_epoch=FLAGS.n_e, batch_size=FLAGS.b_s, verbose=FLAGS.verbose)
    # evaluate the model
    scores = model.evaluate(x_data, y_data)
    print("%s: %.2f" % (model.metrics_names[1], scores[1]))

    est = model.predict(x_data)

    # Make graph
    if FLAGS.graph == 1:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        fig, ax1 = plt.subplots()
        k = range(1, y_data.shape[0] + 1)
        ax1.plot(k, y_data, 'b-')
        ax1.plot(k, est, 'r-')
        ax1.set_xlabel('time')
        ax1.set_ylabel('energy', color='b')
        ax1.tick_params('y', colors='b')

        ax2 = ax1.twinx()
        ax2.plot(k, xy[:, -2], 'r:')
        ax2.set_ylabel('velocity', color='r')
        ax2.tick_params('y', colors='r')

        fig.tight_layout()
        plt.savefig('plot.pdf')


