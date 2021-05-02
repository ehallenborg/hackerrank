#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def builtinversion_extraLongFactorials(n):
    print(math.factorial(n))
    return math.factorial(n)

def reducedextraLongFactorials(n):
    print(reduce(lambda x, y: x*y, range(n+1)[1:]))
    return reduce(lambda x, y: x*y, range(n+1)[1:])

def fact(n):
    if(n==1):
        return 1
    prod=n*fact(n-1)
    return prod

def seperatefunctionsextraLongFactorials(n):
    n = fact(n)
    print(n)
    return n

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
