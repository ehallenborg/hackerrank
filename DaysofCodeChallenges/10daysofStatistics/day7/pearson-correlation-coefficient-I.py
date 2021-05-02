# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = list(map(float,input().strip().split()))
y = list(map(float,input().strip().split()))

stdv_x = (sum([(i - sum(x)/n)**2 for i in x]) / n)**0.5
stdv_y = (sum([(i - sum(y)/n)**2 for i in y]) / n)**0.5

cov = sum([(x[i] - sum(x)/n) * (y[i] - sum(x)/n) for i in range(n)])

coeff = cov / (n * stdv_x * stdv_y)

print(round(coeff, 3))

