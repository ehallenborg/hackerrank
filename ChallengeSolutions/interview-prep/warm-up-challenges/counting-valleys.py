#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    current_height = 0
    prev_height = 0
    output = 0

    for i in range(n):
        if (s[i] == 'U'):
            current_height += 1
        elif s[i] == 'D':
            current_height -= 1
        if current_height == 0 and prev_height < 0:
            output += 1
        prev_height = current_height
       
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
