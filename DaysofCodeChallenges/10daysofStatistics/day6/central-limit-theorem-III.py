'''
You have a sample of 100 values from a population with mean 500 and 
with standard deviation 80.
Compute the interval that covers the middle 95% of the distribution of the sample mean.
In other words, compute A and B such that P(A<x<B) = 0.95.
Use the value of z=1.96. Note that z is the z-score.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
mean = int(input())
stdev = int(input())
prob = float(input())
z = float(input())

stdev_ = stdev / (n**0.5)
print(round(mean - stdev_*z,2))
print(round(mean + stdev_*z,2))
