def HOA(s):
    cnt_upper, cnt_lower = 0, 0
    for char in s:
        if(char.isupper()):
            cnt_upper+=1
        else:
            cnt_lower+=1
    print(f"upper case: {cnt_upper} \nlower case: {cnt_lower}")

s = input()
Hoa(s)