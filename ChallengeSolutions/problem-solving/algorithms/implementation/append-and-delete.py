#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    min_len = min(len(s), len(t))
    same_char = 0

    if ''.join(set(s)) == ''.join(set(t)) or len(s) + len(t) < k:
        return "Yes"

    for i in range(min_len):
        if s[i] != t[i]:
            same_char = i
            break

    diff = (len(s) - same_char) + (len(t) - same_char)

    if (diff <= k and (diff - k) % 2 == 0):
        return "Yes"
    else:
        return "No"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
