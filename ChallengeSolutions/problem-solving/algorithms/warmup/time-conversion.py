#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    convert = s.split(":")
 
    if s[-2:] == "PM" and convert[0] != "12":
        convert[0] = str(int(convert[0]) + 12)
    elif s[-2:] == "AM" and convert[0] == "12":
        convert[0] = "00"

    convert = ":".join(convert)

    return str(convert)[:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
