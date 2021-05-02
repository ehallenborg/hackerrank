#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    j = n-1
    store = arr[j]
    while j > 0 and arr[j-1] > store:
        arr[j] = arr[j-1]
        print(" ".join(str(x) for x in arr))
        j = j - 1
    arr[j] = store
    print(" ".join(str(x) for x in arr))


def insertionSortMethod2(n, arr):
    store = arr[-1]
    j = n-2
    
    while (store < arr[j]) and (j >= 0):
        arr[j+1] = arr[j]
        print(' '.join(map(str, arr)))
        j = j - 1
        
    arr[j+1] = store
    print(' '.join(map(str, arr)))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
