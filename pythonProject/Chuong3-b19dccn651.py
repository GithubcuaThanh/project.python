#3-1.
friends = ['Tuyen','Nghia','Alex','Hoang']
a = friends[0:]
print(a)
print("\n")

#3-2
mess = ['Hi','Hello','Chao','Bye']
for mes in mess:
    for friend in friends:
        print(f"{mes} {friend}")
print("\n")

#3-3
a = ['may bay','tau','xe may']
for x in a:
    print(f"Toi muon co mot chiec {x.title()}")
print("\n")
#3-4
for i in friends:
    print(f"Toi nay di an voi toi nhe {i.title()}")
print("\n")

#3-5
print(friends[0].title())
friends[0] = 'Nam'
print(friends)
for i in friends:
    print(f"Toi nay di an voi toi nhe {i.title()}")
print("\n")

#3-6
for i in friends:
    print(f"Toi da tim duoc mot ban lon hon roi {i.title()}")
friends.insert(0, 'Thu')
friends.insert(3, 'Trang')
for i in friends:
    print(f"Toi nay di an voi toi nhe {i.title()}")
print("\n")

#3-7
print(friends)
print("Do co su co nen toi nay t khong the moi tat ca cac ban den choi")
popped_friends = friends.pop()
print(friends)
print(popped_friends)
del friends[0:]
print(friends)
print("\n")

#3-8
street = ['Dong anh', 'Ha Dong', 'Pho Co', 'Thanh Xuan', 'Cau Giay']
print(street)
print(sorted(street))
print(street)
print(sorted(street, reverse=True))
print(street)
street.reverse()
print(street)
street.reverse()
print(street)
street.sort()
print(street)
street.sort(reverse=True)
print(street)
print("\n")

#3-9
print(len(street))
print("\n")

#3-10
list = ['Nui', 'Doi', 'Song', 'Cay', 'Hoa']
for i in list  :
    print(i)
print("\n")

#3-11
pizza = ['Pizza Bo Bolognese','Pizza Hawaii','Pizza chuc chich']
for i in pizza:
    print(i)

for i in pizza:
    print(f"T thich an {i.title()}")
print("\n")

#3-13
for value in range(1,21):
    print(value)
print("\n")

#3-14
x = [a for a in range(1,1000001)]
# for i in x:
#     print(i)

#3-15
print(min(x))
print(max(x))
tong = sum(x)
print(tong)
print("\n")

#3-16
for value in range(1,21,2):
    print(value)
print("\n")
# for i in value:
#     print(i)

# 3-21
for i in pizza:
    print(i)
friend_pizza = pizza[:]
pizza.append('pizza normal')
friend_pizza.append('pizza medium')
print(pizza)
print(friend_pizza)
print("\n")

# 3-23
restauran = ('thit', 'rau', 'dich vu', 'nam', 'ruou')
for i in restauran:
    print(i)
    restauran = ('thit', 'rau', 'hai san', 'tom hum', 'ca chien')
for i in restauran:
    print(i)



