#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):    
    val = max(arr)
    arr.sort()

    for i in range(len(arr)-k+1):
        val = min(val, arr[i+k-1] - arr[i])

    # min([(arr[i+k-1]-arr[i]) for i in range(len(arr)-k+1)])
    return val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
