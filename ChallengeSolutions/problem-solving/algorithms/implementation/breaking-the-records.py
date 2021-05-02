#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_score = max_score = scores[0]
    min_change = max_change = 0

    for i in scores:
        if i < min_score:
            min_score = i
            min_change += 1
        if i > max_score:
            max_score = i
            max_change += 1
    
    return max_change, min_change

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
