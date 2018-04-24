#!/usr/bin/env bash
for i in `ps -ef | grep python | grep web.py | awk '{print $2}'`
do
    kill ${i}
done
nohup python web.py -sconf.properties &
tail -200f ~/nohup.out
