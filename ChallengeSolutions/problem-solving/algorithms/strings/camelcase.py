#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    total = 1
    for i in s:
        if i.isupper():
            total += 1
    return total

def onelinercamelcase(s):
    return( sum(map(str.isupper, s)) + 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
