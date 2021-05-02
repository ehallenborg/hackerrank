'''
The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of 2.4 and a standard deviation of 2.0.

A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import erf

x = int(input())
n = int(input())
mean = float(input())
stdev = float(input())

stdev_ = stdev * n**0.5

cdf = 0.5 * (1 + erf((x - mean * n) / (stdev_ * 2**0.5)))

print(round(cdf,4))