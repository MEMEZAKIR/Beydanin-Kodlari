import re

Dogumtarihi = "2005"
Karakterler = ["\@,\€,\+,\*,\?,\!"]

def şifre_kontrol(şifre):
    if len (şifre) < 8:
        raise Exception(" Şifre 8 karakterden fazla olmalıdır. ")
    if not re.search("[a-z]",şifre):
        raise Exception(" en az 1 tane küçük harf olmalı")
    if not re.search("[0-9]", şifre):
        raise Exception(" en az 1 tane rakam girmelisin")
    if not re.search(str(Karakterler), şifre):
        raise Exception(" en az bir özel (\@,\€,\+,\*,\?,\!) karakter girmelisin")
    if not re.search("[A-Z]", şifre):
        raise Exception("en az 1 büyük harf girmelisin.")
    if re.search(Dogumtarihi, şifre):
        raise Exception("şifrene doğum tarihini ekleyemezsin")
   # elif şifre.startswith(Dogumtarihi) == True:
    #    print("şifreniz doğum tarihiyle başlayamaz")
   # elif şifre.endswith(Dogumtarihi) == True:
    #    print("şifreniz doğum tarihiyle bitemez")
        
    else:
        print("şifreniz oluşturuldu")
        

while True:
    try:
        şifre = input("şifre gir")
        şifre_kontrol(şifre)

    except Exception as Hata:
        print(Hata)
        
    else:
        break

