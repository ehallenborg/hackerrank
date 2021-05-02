#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    answer = []

    for i in range(len(p)):
        ind = p.index(i + 1)
        new_ind = p.index(ind + 1)
        answer.append(new_ind + 1)

    return answer

def permutationEquationOneLiner(p):
    return [p.index(p.index(i+1)+1)+1 for i in range(len(p))]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    
