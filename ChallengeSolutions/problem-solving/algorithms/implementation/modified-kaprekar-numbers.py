#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    count = []
    for i in range(p, q+1):
        sqr = i**2
        string = str(sqr)
        
        r = string[-len(str(i)):]
        l = string[:-len(str(i))]

        if not l:
            l = '0'

        if int(r)+int(l) == i:
            count.append(i)
    
    if count:
        for i in count:
            print(i, end=' ')
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
