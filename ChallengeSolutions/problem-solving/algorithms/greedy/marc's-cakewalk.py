#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    calorie.sort(reverse = True)
    min_mile = 0
    for i in range(len(calorie)):
        min_mile += (2**i) * calorie[i]

    return min_mile

def marcsCakewalkshorter(calorie):
    calorie.sort(reverse = True)
    return sum([(calorie[i] * (2**i)) for i in range(len(calorie))])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
