#!/usr/bin/python3

from re import A


a = 89
b = 10
temp = 0

temp = a
a = b
b = temp

print("a={:d} - b={:d}".format(a, b))
