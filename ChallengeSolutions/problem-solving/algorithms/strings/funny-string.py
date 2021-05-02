#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    s_rev=''.join(reversed(s))
    a, b = [], []

    for i in range(1, len(s)):
        a.append( abs(ord(s[-i]) - ord(s[-(i+1) ])) )
        b.append( abs(ord(s_rev[-i]) - ord(s_rev[-(i+1) ])) )

    return "Funny" if a == b else "Not Funny"

def funnyStringShortandSweet(s):
    arr = [abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s) - 1)]
    return "Funny" if arr == arr[::-1] else "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
