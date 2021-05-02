'''
The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the first 5 inspections?

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

n, d = list(map(float, input().split(" ")))
v = int(input())

print(round(1 - (1 - (n / d))**v, 3))
