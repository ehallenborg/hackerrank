# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
arr = list(map(int, input().split()))

mean = sum(arr)/n
variance = sum(((x - mean) ** 2) for x in arr) / n

print(round(variance**0.5, 1))