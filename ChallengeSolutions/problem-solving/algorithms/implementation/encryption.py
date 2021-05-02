#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s.strip()
    #floor = math.floor(len(s)**0.5)
    ceil = math.ceil(len(s)**0.5)
    string = ''

    for i in range(ceil):
        string = string + (s[i::ceil]) + " "

    return string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
