#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def reverse(num):
    test_num = 0

    while(num>0):
        remainder = num % 10
        test_num = (test_num * 10) + remainder
        num = num//10

    return test_num
 
def beautifulDays(i, j, k):
    beautiful = 0

    for q in range(i, j+1):
        switch = reverse(q)

        if abs(q - switch) % k == 0:
            beautiful += 1
    
    return beautiful

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
