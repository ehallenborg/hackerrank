import statistics as st

n = int(input())
arr = list(map(int, input().split()))
freq = list(map(int, input().split()))

data = []
for i in range(n):
    data += [arr[i]] * freq[i]
N = sum(freq)
data.sort()

if n%2 != 0:
    q1 = st.median(data[:N//2])
    q3 = st.median(data[N//2+1:])
else:
    q1 = st.median(data[:N//2])
    q3 = st.median(data[N//2:])

print(round(float(q3-q1), 1))