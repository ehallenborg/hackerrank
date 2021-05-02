'''
A large elevator can transport a maximum of 9800 pounds.
 Suppose a load of cargo containing 49 boxes must be transported via the elevator. 
 The box weight of this type of cargo follows a distribution with a mean of 205 pounds and a standard deviation of 15 pounds. 
 Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import erf

x = int(input())
n = int(input())
mu = int(input())
sigma = int(input())

mu_ = n * mu
sigma_ = n**0.5 * sigma
Z = (x - mu_)/sigma_

print(round(0.5*(1+erf(Z/2**0.5)), 4))