#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1,x2, v2):
    # x2 will always start ahead so if v2 is also higher than v1, x1 will never catch up
    if (x2 - x1) * (v2 - v1) < 0 and (x2 - x1) % (v2 - v1) == 0:
        return "YES"
    else:
        return "NO"

def kangaroo_long(x1, v1, x2, v2):
    answer = "NO"

    # the long way is to have the kangaroos take each jump within the defined limits
    # and see if they ever meet
    for n in range(1, 10000):
        x1 = x1 + v1
        x2 = x2 + v2
        
        if (x1 == x2):
            answer = "YES"
            break
    
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
