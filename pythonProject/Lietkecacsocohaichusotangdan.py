s = input()
a = set()

for i in range(1, len(s), 2):
    a.add(int(s[i-1])*10 + int(s[i]))
a = sorted(a)
for i in a:
    print(i, end = ' ')