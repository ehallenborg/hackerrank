#!/bin/python3
import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def LCM(a, b):
    return (a*b)//math.gcd(a,b)

def getTotalX(a, b):
    count = 0
    leastcommon = reduce(LCM, a)
    greatcommon = reduce(math.gcd, b)

    while leastcommon <= greatcommon:
        if(greatcommon % leastcommon) == 0:
            count += 1
        leastcommon = leastcommon + reduce(LCM, a)

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
