'''
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

No more than 2 rejects?
At least 2 rejects?
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

l, r = list(map(float, input().split(" ")))

print(round(sum([b(i, 10, 0.12) for i in range(0, 3)]), 3))

print(round(sum([b(i, 10, 0.12) for i in range(2, 11)]), 3))

