
#---Bir "Hata" yapısının oluşabileceği satırlar "try" yapısı altına konumlandırılmalıdır.
#---"except",olası hata durumunda yapılacakların belirtildiği bölüm/ler.


def ilk_örnek():
    try:
        x=int(input("aklıma fikir gelmedi vıdıvıdı"))
        if x == 0:
            raise Exception("canım sıkıldı, o yüzden 0 değeri giremezsin")
    except Exception as Hata:  #---ikisini birlikte kullanabilirsin(raise ve except)
        print(" bir hata yaptın ", Hata)  
    else:
        print(" bir sayı girdin")
    finally:
        print("bu kısım bitti.(finally altında yeni şeyler yazmana gerek yok, try ile aynı hizada yazmaya dewam edebilirsin)")

def ikinci_örnek():
    def kontrol(x):
        if x.isdigit() == False:
            raise Exception("yalnızca rakam girebilirsin")
        elif len(x)<5:
            raise Exception("5 den az değer giremezsin")

    try:
        x = input("bir şifre gir('5 den fazla değeri olmalı')")
        kontrol(x)
    except Exception as Hata1:
        print(Hata1)
    else:
        print(f"girdiğiniz değer {x}")
        ilk_örnek()

ikinci_örnek()

