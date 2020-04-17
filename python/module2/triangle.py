#! /usr/bin/python3

import sys
from math import sqrt
try:
    a, b, c = [int(x) for x in sys.argv[1:4]]
except ValueError:
    print("You need to pass three integers")
    exit(1)

p = (a + b + c)/2

try:
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print(s)
except ValueError:
    print("Incorrect triangle sides size")


