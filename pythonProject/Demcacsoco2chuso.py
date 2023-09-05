s = input()
a = {}
for i in range(1, len(s), 2):
    so = int(s[i-1])*10+int(s[i])
    if so not in a:
        a[so] = 1
    else: a[so] += 1
for i in a.keys():
    print(str(i) + " " + str(a[i]))