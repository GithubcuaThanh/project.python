def isLuckyNumber(s):
    for i in s:
        if i != '4' and i != '7':
            return 'NO'
    return 'YES'

T = int(input())
for t in range(T):
    print(isLuckyNumber(s=input()))