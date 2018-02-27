#coding=utf-8

import random
import math
import time

print 'Hello World!',

print 2**65

for c in 'python':
    if c == 'h':
        pass
    else:
        print c+c+c

x = range(10)
print x
xx = random.choice(x)
print(xx)

a = b = 1
print a is b
print a is not b

print math.pi
print math.e

print "当前时间戳为:", long(time.time() * 1000)


def hello(str):
    print 'Hello '+str


hello(raw_input('YOUR NAME \n'))
