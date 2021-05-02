#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    new = [0 for i in range(len(a))]

    n = len(a)
    for i in range(0,n):
        if i+k <n:
            new[i+k] = a[i]
        else:
            new[(i+k)%n] = a[i]

    j = 0
    for i in queries:
        queries[j] = new[i]
        j += 1

    return queries

def builtinfunctioncircularArrayRotation(a, k, queries):
    # remember to import deque
    dq = deque(a, len(a))
    dq.rotate(k)
    
    return [dq[num] for num in queries]

def shift_right(lst):
    try:
        return [lst[-1]] + lst[:-1]
    except IndexError:
        return lst

def timeoutcircularArrayRotation(a, k, queries):
    i = 0
    values = []

    while i < k:
        a = shift_right(a)
        i += 1

    for j in queries:
        values.append(a[j])
    
    return values

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
