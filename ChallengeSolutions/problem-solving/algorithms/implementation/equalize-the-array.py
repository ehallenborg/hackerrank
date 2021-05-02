#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    count = len(arr)
    
    for i in set(arr):
        count = min(len(arr) - arr.count(i), count)

    return count

def equalizeArrayoneline(arr):
    return ( min( [ len(arr) - arr.count(i)  for i in set(arr) ]) )

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
