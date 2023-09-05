T = int(input())
for t in range(T):
    so = input()
    length = len(so)
    if length >= 4 and so[0] == so[length - 2] and so[1] == so[length - 1]:
        print('YES')
    else:
        print('NO')