import math

T = int(input())

for t in range(T):
    res = 0
    n = int(input())
    n = n * 2
    for i in range(2, int(math.sqrt(n))+1):
        if n % i != 0:
            continue
        j = n // i
        if (i+j-1) % 2 == 0:
            cuoi = (i+j-1)//2
            dau = j - cuoi
            if (dau != cuoi):
                res += 1
    print(res)