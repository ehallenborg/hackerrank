# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
In a certain plant, the time taken to assemble a car is a random variable, X, having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. What is the probability that a car can be assembled at this plant in:

Less than 19.5 hours?
Between 20 and 22 hours?
'''

from math import exp
lamd = float(input())
k = int(input())

def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def pos(miu, x):
    return ((miu ** x) * exp(-miu)) / fact(x)

print(round(pos(lamd, k), 3))
