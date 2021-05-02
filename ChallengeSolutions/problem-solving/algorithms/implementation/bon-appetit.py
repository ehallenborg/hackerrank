#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    '''
    bill: an array of integers representing the cost of each item ordered
    k: an integer representing the zero-based index of the item Anna doesn't eat
    b: the amount of money that Anna contributed to the bill
    '''
    annabill = bill.copy()
    annabill.pop(k)

    if (sum(annabill)%b) == 0:
        result = "Bon Appetit"
    else:
        result = int((sum(bill) - sum(annabill))/2)

    print(result)

    return result

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
