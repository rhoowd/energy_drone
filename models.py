#!/usr/bin/env python
#coding=utf8
from keras.layers import Dense
import config


FLAGS = config.flags.FLAGS


def base_model(model):
    model.add(Dense(12, input_dim=FLAGS.n_h, init='uniform', activation='relu'))
    model.add(Dense(15, init='uniform', activation='relu'))
    model.add(Dense(15, init='uniform', activation='relu'))
    model.add(Dense(1, init='uniform', activation='relu'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_squared_error'])


def flexible_model(model):
    if FLAGS.depth < 2:
        print "depth should be larger than 1"
        exit()

    model.add(Dense(FLAGS.h_size, input_dim=FLAGS.n_h, init='uniform', activation='relu'))
    for i in range(FLAGS.depth - 2):
        model.add(Dense(FLAGS.h_size, init='uniform', activation='relu'))
    model.add(Dense(1, init='uniform', activation='relu'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_squared_error'])

