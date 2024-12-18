class Müşteri:
    def __init__(self,ad,soyad,şifre,hesapbakiye,kredikartborç):
        self.ad=ad
        self.soyad=soyad
        self.şifre=şifre
        self.hesapbakiye=hesapbakiye
        self.kredikartborç=kredikartborç

class ATM:
    def __init__(self):
        self.döngü=True
        self.kişisel_hesap_bilgileri = []
        self.kullanıcı_Listesi = []
    

    def program(self):
        secim=self.menu()
        if secim==1:
            self.hesapekleme()
        elif secim==2:
            self.hesapgörüntüle()
        elif secim==3:
            self.döngü=False
            exit()


    def menu(self):
        secim=int(input(" Hesap ekleme[1] \n Hesap görüntüleme[2] \n Çıkmak için[3]\n Seçiminiz: "))
        
        while secim<1 or secim>3:
            print("Lütfen 1 ile 3 arasında değer giriniz \n")
            self.program()
        return secim

    def Yeni_müşteri(self):
        self.ad=input("\n Adınızı girin: ")
        self.soyad=input(" Soyadınızı girin: ")
        self.şifre=input(" Şifrenizi girin: ")
        self.hesapbakiye=input(" Hesap bakiyenizi girin: ")
        self.kredikartborç=input(" Borcunu gir: ")
        return Müşteri(self.ad,self.soyad,self.şifre,self.hesapbakiye,self.kredikartborç)

    def hesapekleme(self):

        kullanıcı_bilgiler = self.Yeni_müşteri()
        hesap_başlığı = kullanıcı_bilgiler.ad
        self.kişisel_hesap_bilgileri.append(kullanıcı_bilgiler)
        self.kullanıcı_Listesi.append(hesap_başlığı)
        print("\n Yeni hesabınız başarıyla oluşturulmur {} bey/hanım \n ".format(hesap_başlığı))
        self.program()

        return kullanıcı_bilgiler, self.kullanıcı_Listesi

    
    def hesapgörüntüle(self):


        if not self.kullanıcı_Listesi:
                print("\n Henüz hiç kullanıcı oluşturulmamış.")
        else:
                print("\n Görüntülemek istediğiniz hesabın şifresini girin \n ")
                girilen_şifre = input( self.kullanıcı_Listesi )
                found = False
                for kullanici in self.kişisel_hesap_bilgileri:
                    if kullanici.şifre.lower() == girilen_şifre.lower():
                        print(f"\n \n Ad: {kullanici.ad} Soyad: {kullanici.soyad} Şifre: {kullanici.şifre} Bakiye: {kullanici.hesapbakiye} Borç: {kullanici.kredikartborç}\n")
                        found = True
                        break
                if not found:
                    print(f"'{girilen_şifre}' şifresi tanımlanamadı.")
        
        self.program()
    

Banka=ATM()
while Banka.döngü:
    Banka.program()