T = int(input())
for t in range(T):
    n = int(input())
    a1 = list(int(i) for i in input().split())
    a2 = list(int(i) for i in input().split())
    a1.sort()
    a2.sort()
    check = 'YES'
    for i in range(0, n):
        if a1[i] > a2[i]:
            check = 'NO'
            break
    print(check)