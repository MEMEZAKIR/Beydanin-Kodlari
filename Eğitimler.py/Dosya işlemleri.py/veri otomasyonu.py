
import re
import time
import sys

class Veri_Otomasyonu:
    def __init__(self, uygulama_ad):
        self.uygulama_ad=uygulama_ad
        self.dongu = True
    
    def menu(self):
        def secim_kontrol(secim):
            if re.search("[^1-4]",secim):
                raise Exception("\n 1 ile 4 arasında bir değer girmelisin")
            elif len(secim)!=1:
                raise Exception("\n 1 ile 4 arasında bir değer girmelisin")
            
        while True:
            try:
                secim = input("\n [1]-kayıt ekleme \n [2]-kayıt silme \n [3]-kayıt okuma \n [4]-çıkmak için \n")
                secim_kontrol(secim)
            except Exception as Hata:
                print("\nbir hata yaptınız", Hata)
            else:
                break
        return secim

    def program(self):
        secim=self.menu()

        if secim == "1":
            print("kayıt ekleme menüsüne yönlendiriliyorsunuz",end="")
            for i in range(5):
                time.sleep(.5)
                print(".", end="",flush=True)
            time.sleep(.7)
            self.kayit_ekleme()

        if secim == "2":
            print("kayıt silme menüsüne yönlendiriliyorsunuz",end="")
            for i in range(5):
                time.sleep(.5)
                print(".", end="",flush=True)
            time.sleep(.7)
            self.kayit_silme()

        if secim == "3":
            print("kayıt okuma menüsüne yönlendiriliyorsunuz",end="")
            for i in range(5):
                time.sleep(.5)
                print(".", end="",flush=True)
            time.sleep(.7)
            self.kayit_okuma()
        
        if secim == "4":
            print("uygulama kapanıyor",end="")
            for i in range(5):
                time.sleep(.5)
                print(".", end="",flush=True)
            time.sleep(.7)
            self.cikis()

    def kayit_ekleme(self):
        print("\n\n---------------------------------------\n Kayıt ekleme menüsüne hoşgeldiniz.")
        def Ad_kontrol(Ad):
            if Ad.isalpha() == False: #---içeriği tamamen karakterlerden oluşuyorsa "True" döndürür 
                raise Exception("\n Adınız sadece Alfabetik karakterlerden oluşmalıdır. ")
        
        while True:
            try:
                Ad = input("\n Adınızı giriniz. ")
                Ad_kontrol(Ad)
            except Exception as Ad_Hata:
                print("\n bir hata yaptın. ", Ad_Hata)
            else:
                
                break

        def Soyad_kontrol(Soyad):
            if Soyad.isalpha() == False:
                raise Exception("\n Soyadınız sadece Alfabetik karakterlerden oluşmalıdır. ")
        while True:
            try:
                Soyad = input("\n Soyadınızı girin. ")
                Soyad_kontrol(Soyad)
            except Exception as Soyad_Hata:
                print("\n bir hata yaptın. ", Soyad_Hata)
            else:
                break
        
        def Yas_kontrol(Yas):
            if len(Yas)>3:
                raise Exception("\n 100 yaşından büyük büyük olamazsıınız. ")
            elif Yas.isdigit() == False:
                raise Exception("\n yaşınız yalnızca rakam değerlerden oluşabilir. ")
            
        while True:
            try:
                Yas = input("\n Yaşınızı giriniz. ")
                Yas_kontrol(Yas)
            except Exception as Yas_Hata:
                print("\n bir hata yaptınız ", Yas_Hata)
            else:
                break
        
        def TC_kontorl(Tc):
            if len(Tc)!=11:
                raise Exception("\n TC kimlik numaranız 11 hanleli olmalı")
            elif Tc.isdigit() == False:
                raise Exception("\n yaşınız yalnızca rakam değerlerden oluşabilir. ")
        while True:
            try:
                Tc = input("\n TC'nizi giriniz. ")
                TC_kontorl(Tc)
            except Exception as Tc_Hata:
                print("\n bir hata yaptınız. ", Tc_Hata)
            else:
                break
        def Mail_kontrol(Mail):
            if not re.search("@gmail.com" or "@hotmail.com", Mail):
                raise Exception("\n mailinizde '@gmail.com' ya da '@hotmail.com' ibaresi bulunmalıdır. ")
        while True:
            try:
                Mail = input("\n Mailinizi giriniz. ")
                Mail_kontrol(Mail)
            except Exception as Mail_hata:
                print("\n bir hata yaptınız.", Mail_hata)
            else:
                break
        
        #---öncelikle dosyada okuma işlemi yaparız. Eğerki dosya boşsa, id işlemini 1 den başlatırız

        with open("C:/Users/user/Desktop/Veri_Otomasyonu.txt", "r", encoding="utf-8") as Veri_tabanı:
            satır_sayısı = Veri_tabanı.readlines()
        if len(satır_sayısı) == 0:
                Id = 1
        else:
            with open("C:/Users/user/Desktop/Veri_Otomasyonu.txt", "r", encoding="utf-8") as Veri_tabanı:
                    Id = int(Veri_tabanı.readlines()[-1].split("-")[0])+1
        #1-)Dosya tekrar okunuyor ve Id, dosyadaki son satırın ilk kısmına göre belirleniyor.
        #2-)Veri_tabanı.readlines()[-1] ifadesi, dosyanın son satırını alıyor.
        #3-)split("-")[0], satırı "-" karakterine göre ayırarak ilk elemanı seçiyor. Bu ilk eleman genellikle bir numarayı temsil eder.
        #4-)Son olarak int(...)+1 ile bu numara bir artırılıyor ve yeni Id değeri olarak atanıyor.

        with open("C:/Users/user/Desktop/Veri_Otomasyonu.txt", "a+", encoding="utf-8") as Veri_tabanı:
            Veri_tabanı.write("\n{}-{} {} {} {} {}".format(Id,Ad,Soyad,Yas,Mail,Tc))
        print("Veriler işlenmiştir...")       
        self.program()

            
             
    def kayit_silme(self):
        silinecek_Id = input("\n Bütün verileri silmek için-[0]\n ya da\n Silmek istediğiniz kişinin Id numarasını giriniz: ")
        with open("C:/Users/user/Desktop/Veri_Otomasyonu.txt", "r", encoding="utf-8") as Veri_tabanı:
            Id_Listesi = []
            Veri_tabanı_Listesi = Veri_tabanı.readlines()
            for i in range(0,len(Veri_tabanı_Listesi)):
                Id_Listesi.append(Veri_tabanı_Listesi[i].split("-")[0])

        if silinecek_Id=="0":

            with open("C:/Users/user/Desktop/Veri_Otomasyonu.txt", "w", encoding="utf-8") as Yeni_Veri_tabanı:
                Yeni_Veri_tabanı.truncate(0)
            print("Tüm veriler başarıyla silinmiştir.")

        else:
            del Veri_tabanı_Listesi[Id_Listesi.index(silinecek_Id)]

            with open("C:/Users/user/Desktop/Veri_Otomasyonu.txt", "w", encoding="utf-8") as Yeni_Veri_tabanı:
                for i in Veri_tabanı_Listesi:
                    Yeni_Veri_tabanı.write(i)
                print("Kayıt siliniyor",end="")
                for i in range(5):
                    time.sleep(.5)
                    print(".", end="",flush=True)
                time.sleep(.7)
                print("Kayıt Başarıyla silinmiştir...")
        self.program()
            
            

    def kayit_okuma(self):
        with open("C:/Users/user/Desktop/Veri_Otomasyonu.txt", "r", encoding="utf-8") as Veri_tabanı:
            secimm = input("\n Okuma işlemi yapmak istediğiniz kişinin Id'sini giriniz \n Bütün kişilerin bilgilerini görüntülemek için-[0]: ")
            Veri_tabanı_Listesi = Veri_tabanı.readlines()
            
            if len(Veri_tabanı_Listesi) == 0:
                print("Veri tabanı boş.")
            elif secimm == "0":
                for i in Veri_tabanı_Listesi:
                    print(i)
            else:
                Id_Listesi = []
                for i in Veri_tabanı_Listesi:
                    Id_Listesi.append(i.split("-")[0])  
                    
                if secimm in Id_Listesi:
                    print(Veri_tabanı_Listesi[Id_Listesi.index(secimm)])
                else:
                    print(f"ID {secimm} bulunamadı.")
                    
        self.program()
                    
#--- Düzelt şunu

    def cikis(self):
        print("\nUygulama kapanıyor",end="")
        for i in range(5):
            time.sleep(.5)
            print(".",end="", flush=True)
        time.sleep(.7)
        print("Teşekkürler")
        Sistem.dongu=False
        sys.exit()


Sistem = Veri_Otomasyonu("Beydan Otomasyon_Sistemi")
while Sistem.dongu:
    Sistem.program()