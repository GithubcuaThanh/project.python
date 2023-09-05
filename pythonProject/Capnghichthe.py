n = int(input())
a = list(int(i) for i in input().split())
count = 0
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[j] < a[i]:
            count += 1
print(count)