#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    highest = -100000000000
    for j in range(len(arr) - 2):
        for i in range(len(arr[j]) - 2):
            highest = max(highest, (
                arr[i][j] +
                arr[i][j+1] +
                arr[i][j+2]+
                arr[i+1][j+1] +
                arr[i+2][j] +
                arr[i+2][j+1] +
                arr[i+2][j+2]
            ))
            print(highest)
    return(highest)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
