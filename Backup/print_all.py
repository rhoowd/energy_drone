#!/usr/bin/env python
#coding=utf8
"""

# Data format

- Location: data['loc']['lat'], data['loc']['lng'], data['loc']['alt']
- Power:
  - data['V']: Voltage
  - data['I']: Current
  - data['capacity']: Remaining energy
  - data['percent']: Remaining energy (%)
  - data['full']: Full battery capacity
- Drone status:
  - data['vx']: Velocity in X axis
  - data['vy']: Velocity in Y axis
  - data['vz']: Velocity in Z axis
  - data['yaw']: Direction (degree)

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
        v = math.sqrt(pow(data['vx'],2) + pow(data['vy'],2))
        print cnt, v * sign(data['vx']), -1*data['V']* data['I']/1000000.0, data['vx'], data['vy'], data['V'], data['I'], data['capacity']

finally:
   f.close()