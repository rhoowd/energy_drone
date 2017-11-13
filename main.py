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
from keras.models import Sequential
from keras.layers import Dense


FLAGS = config.flags.FLAGS

if __name__ == '__main__':
    print FLAGS.n_s, FLAGS.n_h