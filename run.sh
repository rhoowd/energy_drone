#!/bin/sh

echo "$1"

for s in 1 2
do
    for hs in 15 30
    do
      for d in 3 6
      do
        for h in 5 10 30 50
        do
          echo "python main.py --f_n $1 --n_h $h --depth $d --n_e 2000  --seed $s --h_size $hs"
        done
      done
    done
done