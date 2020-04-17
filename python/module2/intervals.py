#! /usr/bin/python3

import sys

try:
    n = int(sys.argv[1])
except ValueError:
    raise ValueError("Please pass an integer value")

if -15 < n <= 12 or 14 < n < 17 or n >= 19:
    print("True")
else:
    print("False")
