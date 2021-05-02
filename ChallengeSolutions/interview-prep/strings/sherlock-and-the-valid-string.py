#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the isValid function below.
def isValid(s):
    c = Counter(s)
    print(c)

    freq = Counter(c.values())
    print(freq)

    if len(freq) == 1:
        return "YES"

    elif len(freq) == 2:

        key_max = max(freq.keys())
        key_min = min(freq.keys())

        print(key_max)
        print(key_min)

        if key_max - key_min == 1 and freq[key_max] == 1:
            return "YES"

        elif key_min == 1 and freq[key_min] == 1:
            return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
