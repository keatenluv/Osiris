#!/bin/bash
 
# Change these lists to use the values for offset or interval
declare -a IArray=(1 2 4 8 16 32 64)
declare -a OArray=(1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192)
 
# Change these
file="two.bmp"

for O in ${OArray[@]}; do
    for I in ${IArray[@]}; do
        python3 steg.py -r -B -o$O -i$I -w$file > temp-$O-$I.txt
    done
done