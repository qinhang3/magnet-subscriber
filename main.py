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


def check_pwd(str):
    r = 0
    for cc in str:
        if 'A' <= cc <= 'Z' or 'a' <= cc <= 'z':
            r = r | 1
        if '0' <= cc <= '9':
            r = r | 2
        if cc in "~!@#$%^&*().":
            r = r | 4
    print ('r', r)
    return r


print check_pwd("Ab123.")
