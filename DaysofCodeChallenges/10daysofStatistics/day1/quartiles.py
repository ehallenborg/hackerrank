# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import median

n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()

middle = int(len(arr)/2)

if len(arr)%2 == 0:
    bottom = arr[:middle]
    top = arr[middle:]
else:
    bottom = arr[:middle]
    top = arr[middle+1:]

print(int(median(bottom)))
print(int(median(arr)))
print(int(median(top)))
