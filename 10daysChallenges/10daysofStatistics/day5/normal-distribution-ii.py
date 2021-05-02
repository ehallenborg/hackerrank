# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import erf

def N(mean, std, x):
        return 0.5 + 0.5 * erf((x-mean)/(std* 2**0.5))

print(round( (1- N(70, 10, 80)) * 100, 2))

print(round( (1- N(70, 10, 60)) * 100, 2))

print(round(N(70, 10, 60) * 100, 2))
