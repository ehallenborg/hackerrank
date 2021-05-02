#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    x=int(len(s)/3)
    dropped=0
    y="SOS" *x
    for i in range(len(s)):
        if(s[i]!=y[i]):
            dropped+=1
    return dropped

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
