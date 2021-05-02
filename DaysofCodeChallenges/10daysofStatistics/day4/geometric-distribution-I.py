'''
The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the 5th inspection?

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
def exp(n, p):
    return (1-p)**(n-1)

def g(n, p):
    return exp(n, p) * p

n, d = list(map(float, input().split(" ")))
v = int(input())

print(round(g(v, n/d), 3))
