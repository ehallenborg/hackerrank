#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    # remove duplicates
    scores_single = list(set(scores))
    scores_single.sort(reverse=True)
    pos = []
    l = len(scores_single)

    for i in alice:
        # while there's still positions to check
        # you have to parse through, starting from last element until the value
        # of i is lower than the element being checked
        # return that position
        while (l>0) and (i >= scores_single[l-1]):
            l -= 1
        pos.append(l+1)

    return pos


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
