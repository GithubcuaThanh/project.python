T = int(input())
for t in range(T):
    s = input()
    num = 1
    for i in s:
        if i != '0':
            num *= int(i)
    print(num)