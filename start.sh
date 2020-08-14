#!/bin/sh

mkdir downloads/
echo "aria2 start"
aria2c --enable-rpc --rpc-listen-all --rpc-secret=12345678 --dir=~/downloads/ --seed-time=0 -D
echo "aria2 start pass"