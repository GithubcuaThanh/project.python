T = int(input())
for t in range(0, T):
    s = input()
    s1 = len(s)
    if s1 >= 2 and s[s1-2] == '8' and s[s1-1] == '6':
        print('YES')
    else:
        print('NO')