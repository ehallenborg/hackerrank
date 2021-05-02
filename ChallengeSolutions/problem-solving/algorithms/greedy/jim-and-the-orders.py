#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):

    for i in range(len(orders)):
        orders[i][1] = sum(orders[i])
        orders[i][0] = i + 1

    orders.sort(key = lambda x: x[1])

    return [orders[i][0] for i in range(len(orders))]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
