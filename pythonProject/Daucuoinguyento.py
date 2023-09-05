import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return x > 1

T = int(input())
for t in range(T):
    s = input()
    num1 = s[:3]
    num2 = s[len(s)-3:]
    if isPrime(int(num1)) and isPrime(int(num2)):
        print('YES')
    else: print('NO')