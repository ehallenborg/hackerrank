#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(A):
    # ABC -> BCA -> CAB -> ABC
    # implement a bubble sort-ish and if the number of swaps is even, then yes
    count = 0

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                count += 1

    return "YES" if count % 2 == 0 else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
