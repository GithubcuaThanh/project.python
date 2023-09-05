import math
def nt(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return x > 1

N = int(input())
a = input().split()
dict = {}
for i in a:
    if nt(int(i)):
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
for key, val in dict.items():
    print(str(key) + ' ' + str(val))