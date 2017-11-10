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

This is for analyzing energy consumption of drone

참고
====
 * https://github.com/rhoowd/energy_drone
 * cat data2.dat | tr -d '\n' | perl -pe 's/}{/}\n{/g'

관련 작업자
===========

본 모듈은 다음과 같은 사람들이 관여했습니다:
 * Daewoo Kim



"""
import json
import math


def sign(x):
    if x > 0:
        return 1.
    elif x < 0:
        return -1.
    elif x == 0:
        return 0.
    else:
        return x

f = open("data/f_data.dat")
cnt = 0
try:
    for line in f:
        cnt += 1
        data = json.loads(line)
        v = math.sqrt(pow(data['vx'], 2) + pow(data['vy'], 2))
        k = 5
        if k-0.2 < v < k + 0.2 and 6742 < cnt < 8124 and (-1 * data['V'] * data['I'] / 1000000.0) < 510:
        #if 6742 < cnt < 7258:
            if sign(data['vx']) > 0:
                print '%s\t%s\t%s\t%s' % (cnt, v * sign(data['vx']), -1 * data['V'] * data['I'] / 1000000.0, data['capacity'])
            # print cnt, v * sign(data['vx']), -1 * data['V'] * data['I'] / 1000000.0, data['capacity'], data['vx'], data[
            #     'vy'], data['V'], data['I'], data['capacity']

finally:
   f.close()