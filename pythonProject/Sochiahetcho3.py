T = int(input())
for t in range(T):
    s = input()
    num = 0
    for i in s:
        num += int(i)
    if num % 3 == 0:
        print('YES')
    else: print('NO')