import math

def gcd(a, b):
    while a > 0:
        if a < b:
            a, b = b, a
        a = a % b
    return b

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return x > 1

def sumOfDigits(x):
    sum = 0
    for i in str(x):
        sum = sum + int(i)
    return sum

T = int(input())
for t in range(T):
    a, b = input().split()
    a = int(a)
    b = int(b)
    if isPrime(sumOfDigits(gcd(a,b))):
        print('YES')
    else:
        print('NO')