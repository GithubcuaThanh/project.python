T = int(input())

for t in range(T):
    s = input()
    sum = 0
    pro = 1
    for i in range(0, len(s)):
        if i % 2:
            sum += int(s[i])
        else:
            if s[i] != '0':
                pro *= int(s[i])
    print(pro, sum)