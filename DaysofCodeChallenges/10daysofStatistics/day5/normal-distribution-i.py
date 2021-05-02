# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import erf

def N(mean, std, x):
        return 0.5 + 0.5 * erf((x-mean)/(std* 2**0.5))

print(round( N(20, 2, 19.5), 3))

print(round( N(20, 2, 22) - N(20, 2, 20), 3))