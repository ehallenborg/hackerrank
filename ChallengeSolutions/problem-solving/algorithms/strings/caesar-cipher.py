#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    # abcdefghijklmnopqrstuvwxyz
    new = ''
    for i in s:
        a=65 if i.isupper() else 97
        new = new + ((chr(a+(ord(i)-a+k)%26)) if i.isupper() or i.islower() else i)

    return new


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
