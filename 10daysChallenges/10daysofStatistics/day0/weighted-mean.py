# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
rate = [int(x) for x in input().split()]
weight = [int(x) for x in input().split()]

summing = 0
for i in range(len(rate)):
    summing += (rate[i] * weight[i])

print(round(1.0*summing/sum(weight), 1))