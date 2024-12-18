import requests
import json
import re
import time

#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}


class Site:
    def __init__(self):
        self.dongu = True

    def program(self):
        sehir = input("\n\nLütfen bir şehir ismi giriniz: ")
        APIkey = "c98b175aa4e88d777178b525aa37eac0"
        adres = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric&lang=tr".format(sehir,APIkey)

        Sitee = requests.get(adres)
        antwort = json.loads(Sitee.text)

        
        return antwort, sehir
        
    def menu(self,sehir,antwort):
        secim = input("\n{} hava durumu ile ilgili ne öğrenmek istersiniz...\n  [1]- Anlık Hava Durumu\n  [2]- 1 Aylık Hava Durumu Tahminleri\n  [3]- Yeni Bir Şehir Seçmek\n  [4]-çıkış\n\n".format(sehir))
        
        if secim == "1":
            Hava_Durumu = []

            hava = antwort["weather"][0]["description"] #- weather bir liste, [0] liste içerisindeki ilk sözlüğü seçiyor, 
                                                        #- ["description"] ise sözlüğün "description" anahtarına erişiyor.
            derece =antwort["main"]["temp"]

            Hava_Durumu.append(f"Hava: {hava}")
            Hava_Durumu.append(f"Derece: {derece}")

            for i in Hava_Durumu:
                print(i)

            time.sleep(5)

        elif secim == "2":
            print("bu özelliğimiz şimdilik aktif değil")

        elif secim == "3":
            return "yeni_sehir"
        
        elif secim == "4":
            exit()

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
        


Sistem = Site()
antwort, sehir = Sistem.program()  #- İlk kez şehir bilgilerini alıyoruz

while Sistem.dongu:
    sonuc = Sistem.menu(sehir, antwort)  #- Menüden dönen değeri kontrol et
                                         #- (Menüden dönebilecek tek değer seçim 3. onun dışında aynı şehirle devam ederiz)
    if sonuc == "yeni_sehir":
        antwort, sehir = Sistem.program()  #- Yeni şehir bilgilerini al

#with open("C:/Users/user/Desktop/Havadurumu.txt", "w+", encoding="utf-8") as Dosya:
 #   json.dump(antwort,Dosya)
  #  Dosya.seek(0)
   # print(Dosya.read())