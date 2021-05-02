import math

def is_prime(n):
    if n == 1:
        return False

    else:
        sq = int(math.sqrt(n))
        
        for i in range(2, sq + 1):
            if n % i == 0 and i != n:
                return False

        return True


t = int(input())
for _ in range(t):
    n = int(input())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")
