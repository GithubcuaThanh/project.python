def isPalindrome(x):
    s = str(x)
    if len(s) > 1 and s == s[::-1]:
        return 'YES'
    else:
        return 'NO'

T = int(input())
for t in range(T):
    s = input()
    num = 0
    for i in s:
        num += int(i)
    print(isPalindrome(num))