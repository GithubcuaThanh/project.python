def splitString(s):
    s = s.split('-')
    s.sort()
    print('-'.join(s))

s = input("enter a string: ")
splitString(s)