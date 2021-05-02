#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    if len(s) == 1:
        return "YES"

    count = Counter(s)
    odd = 0

    for i in count:       
        if count[i] % 2 == 1:
            odd += 1
        if odd > 1:
            return "NO"
    
    return "YES"

def gameOfThronesOneLines(s):
    return (sum(s.count(x)%2 for x in set(s) ) <2  and 'YES') or 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
