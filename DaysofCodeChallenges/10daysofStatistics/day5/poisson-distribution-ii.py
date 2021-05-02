# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:

The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating A is C_a = 160 + 40X^2.
The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. The daily cost of operating B is C_b = 128 + 40Y^2.

Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.
'''
def costx(A, B):
    return 160 + 40*(A + A**2)

def costy(A, B):
    return 128 + 40*(B + B**2)

A, B = [float(num) for num in input().split(" ")]

print(round(costx(A,B), 3))
print(round(costy(A,B), 3))
