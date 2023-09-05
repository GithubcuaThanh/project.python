import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return x > 1

T = int(input())
for t in range(T):T = int(input())

for t in range(T):
    s = input()
    sum = 0
    pro = 1
    count0 = 0
    for i in range(0, len(s)):
        if i % 2 == 0:
            sum += int(s[i])
        else:
            if s[i] != '0':
                pro *= int(s[i])
            else: count0 += 1
    if count0 == len(s)//2:
        pro = 0
    print(sum, pro)
    s = input()
    num = s[len(s)-4:]
    if isPrime(int(num)):
        print('YES')
    else: print('NO')