#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    finished = []
    matching = 0

    for i in ar:
        if i not in finished:
            count = ar.count(i)
            print(count)

            pairs = math.floor(count/2)
            matching = matching + pairs

            finished.append(i)
    
    return matching

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
