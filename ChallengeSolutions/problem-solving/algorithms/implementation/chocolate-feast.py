#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    '''
    n: an integer representing Bobby's initial amount of money
    c: an integer representing the cost of a chocolate bar
    m: an integer representing the number of wrappers he can turn in for a free bar
    ----
    w: amt of wrappers (equal to amt of chocolate bought)
    choc: amt of chocolate
    ----
    approach:
    get the amount of chocolate that can initially bought
    check if wrappers generated can then be turned in for a free chocolate
    add in amount of chocolate bought
    take into account the new wrappers generated from newly bought chocolate
    '''

    choc=int(n/c)
    w=int(n/c)

    while w>=m:
        choc += int(w/m)   
        w = int(w/m) + (w%m)

    return(choc)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
