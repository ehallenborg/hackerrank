# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats

length = int(input())
arr = list(map(int, input().split()))

print(np.mean(arr))
print(np.median(arr))
print(int(stats.mode(arr)[0]))
