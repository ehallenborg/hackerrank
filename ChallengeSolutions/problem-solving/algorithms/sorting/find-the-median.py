#!/bin/python3

import math
import os
import random
import re
import sys
import statistics as st

# Complete the findMedian function below.
def findMedianimportedmodule(arr):
    return(st.median(arr))

def findMedian(arr):
    arr.sort()
    return arr[len(arr) // 2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
