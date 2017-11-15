#!/usr/bin/env python
#coding=utf8
from keras.models import Sequential
from keras.layers import Dense
import config
import keras.backend as K
import math


FLAGS = config.flags.FLAGS


# Define metric
def mean_acc(y_true, y_pred):
    return K.mean(1-K.abs(y_true-y_pred)/y_true)


# Models
def base_model():
    model = Sequential()

    model.add(Dense(12, input_dim=FLAGS.n_h, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(15, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(15, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(1, kernel_initializer='uniform', activation='relu'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_squared_error'])

    return model


def flexible_model(input_dim, output_dim=1):
    if FLAGS.depth < 2:
        print "depth should be larger than 1"
        exit()
    model = Sequential()

    model.add(Dense(FLAGS.h_size, input_dim=input_dim, kernel_initializer='uniform', activation='relu'))
    for i in range(FLAGS.depth - 2):
        model.add(Dense(FLAGS.h_size, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(output_dim, kernel_initializer='uniform', activation='relu'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_squared_error', mean_acc])

    return model

def test_model():
    model = Sequential()

    model.add(Dense(12, input_dim=FLAGS.n_h, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(15, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(15, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(1, kernel_initializer='uniform', activation='relu'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_squared_error'])

    return model

