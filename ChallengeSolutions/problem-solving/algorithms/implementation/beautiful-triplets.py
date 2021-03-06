#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    # i < j < k
    # a[j] - a[i]= a[k] - a[j] = d
    trip = 0

    for i in range(len(arr)):
        if arr[i] + d in arr and arr[i]+ 2*d in arr:
            trip += 1

    return trip

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
