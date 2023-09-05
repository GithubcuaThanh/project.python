n = int(input())
arr = []
for i in range(n):
    s = input()
    tmp = []
    for j in s:
        tmp.append(j)
    arr.append(tmp)
res = 0
for i in range(n):
    sl = 0
    for j in range(n):
        if arr[i][j] == 'C':
            res = res + sl
            sl = sl+1

for j in range(n):
    sl = 0
    for i in range(n):
        if arr[i][j] == 'C':
            res = res + sl
            sl = sl +1
print(res)