so = input()
dem = 0
for i in so:
    if i == '4' or i == '7':
        dem = dem + 1
if dem ==4 or dem == 7:
    print('YES')
else:
    print('NO')