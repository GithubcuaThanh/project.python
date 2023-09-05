import re
def no_accent_vietnamese(s):
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[ÍÌỈĨỊ]', 'I', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
    s = re.sub('đ', 'd', s)
    s = re.sub('Đ', 'D', s)
    return s
LUONG_CO_SO=1.49
HE_SO_LUONG=2.34

def tinh_tuoi(namsinh):
    return 2022-namsinh

def email(hoTen):
    l_hoten = hoTen.split()
    so_tu = len(l_hoten)
    hauto = ''
    for i in range(so_tu - 1):
        hauto = hauto + l_hoten[i][0]
    mail = no_accent_vietnamese(l_hoten[-1]) + hauto + '@gmail.com'
    return mail.lower()

def tinh_thang(nam,thang):
    thang_lam_viec = (2022-nam)*12+12-thang
    return thang_lam_viec

def he_so(so_thang_lv):
    num = (so_thang_lv-12)//36
    he_so = HE_SO_LUONG+0.33*(num)
    return he_so

def tinh_luong(nam,thang):
	so_thang_lv=tinh_thang(nam,thang)
	luong_linh=0
	if (so_thang_lv<=12):
		luong_linh=LUONG_CO_SO*0.85*HE_SO_LUONG
	elif so_thang_lv<=48:
		luong_linh=LUONG_CO_SO*HE_SO_LUONG
	else:
		luong_linh=he_so(so_thang_lv)*LUONG_CO_SO
	return(luong_linh)

def tinh_thuong(so_thang,htnv):

	luong_linh=0
	if (so_thang<=12):
		luong_linh=LUONG_CO_SO*0.85*HE_SO_LUONG
	elif so_thang<=48:
		luong_linh=LUONG_CO_SO*HE_SO_LUONG
	else:
		luong_linh=he_so(so_thang)*LUONG_CO_SO
	thuong=0
	if htnv==0:
		he_so_thuong=0.8
	elif htnv==1:
		he_so_thuong=1
	elif htnv==2:
		he_so_thuong=1.2
	elif htnv==3:
		he_so_thuong=1.5
	return luong_linh*he_so_thuong


print(tinh_tuoi(2001))
print(email('Ngo Viet Thanh'))
print(tinh_thang(2021,6))
print(he_so(9))
print(tinh_luong(2021,6))
print(tinh_thuong(12,6))