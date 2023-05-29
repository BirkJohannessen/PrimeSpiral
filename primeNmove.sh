#!/bin/bash

primeRange=$1
scaleDivider=$2
dotRadius=$3

echo $1 $2 $3

python3 PrimeSpiral.py $primeRange $scaleDivider $dotRadius

# python3 PrimeSpiral.py $primeRange $scaleDivider

echo "PRIME_${primeRange}.png"

rm /home/birkj/Desktop/projectWS/birkjohannessencom/src/assets/PRIME_$primeRange.png
mv "PRIME_${primeRange}.png" /home/birkj/Desktop/projectWS/birkjohannessencom/src/assets


