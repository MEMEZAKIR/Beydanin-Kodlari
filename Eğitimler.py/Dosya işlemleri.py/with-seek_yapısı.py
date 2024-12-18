#--- with blok yapısı, bittiği anda dosyayı otomatik kapatır
with open("Erste Datei.txt", "r") as Dosya:

    Dosya.seek(5) #---seek methodu dosyanın okumaya başlayacağı indexi belirler
    
    Dosya.read(15) #---belirtilen indexten sonra 15 indexlik okuma gerçekleştirir, ayrıca yeni indexin yerini söyler
    
    print(Dosya.tell()) #---şu anda hangi indexte kaldığını söyler

#a+,r+