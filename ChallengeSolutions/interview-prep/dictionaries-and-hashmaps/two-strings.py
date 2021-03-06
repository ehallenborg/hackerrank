#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStringsLONG(s1, s2):
    set_1 = ''.join(set(s1))
    set_2 = ''.join(set(s2))

    min_len = min(len(set_1), len(set_2))

    for i in range(min_len):
        if set_1[i] in set_2 or set_2[i] in set_1:
            return "YES"
        
    return "NO"

def twoStringsSpreadOut(s1, s2):
    if set(s1) & set(s2):
        return "YES"
    else:
        return "NO"

def twoStrings(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
