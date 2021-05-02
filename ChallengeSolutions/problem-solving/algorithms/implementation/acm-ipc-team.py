#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


# Complete the acmTeam function below.
def acmTeam_brute_force_time_outs(topic):
    max_subjects = 0
    max_teams = 0

    for i in range(len(topic)):
        list_i = list(topic[i])

        for j in range(i+1, len(topic)):
            subjects = 0
            list_j = list(topic[j])

            for k in range(len(list_i)):
                if list_i[k] != '1':
                    if list_j[k] == '1':
                        subjects += 1
                else:
                    subjects += 1
                
                if subjects > max_subjects:
                    max_subjects = subjects
                    max_teams = 1
                elif subjects == max_subjects:
                    max_teams += 1

    return [max_subjects, max_teams]

def acmTeam(topic):
    lst = []
    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
            x = int(topic[i]) + int(topic[j])
            lst.append(len(str(x))-str(x).count("0"))
        
    return [max(lst), lst.count(max(lst))]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
