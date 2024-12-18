#--- w modulü aynı isimde bir dosya varsa içindeki herşeyi silip yeni girilen ifadeleri yazar
def w_modul():
    Dosya = open("Erste Datei.txt","w")

    Dosya.write(" Hallo, das ist meine erste Datei")

    Dosya.close()

#--- a modülü aynı isimde bir dosya varsa içindekilere dokunmaz, ve kendi değerlerini uygular
def a_modul():
    Dosya = open("Erste Datei.txt","a")

    Dosya.write("\n etwas vıdıdıdıdı")
    
    Dosya.close()

#--- x modulü aynı isimdeki bir dosyayı oluşturmana izin vermez, ve hata verir
def x_modul():
    Dosya = open("Erste Datei.txt","x")

    Dosya.write("\n Hallo, das ist meine erste Datei")
    
    Dosya.close()

#--- r modulü bir dosya üzerinde okuma işlemi gerçekleştirir
def r_modul():
    
    def read(): 
            Dosya = open("Erste Datei.txt", "r")
            print(Dosya.read())#--- "read()"dosyanın tamamında okuma işlemi gerçekleştirir
            print(Dosya.read(5))#--- "read(5)"dosyanın ilk 5 indexi için okuma işemi gerçekleştirir
            Dosya.close()

    def read_line():
      
            Dosya = open("Erste Datei.txt", "r")

            print(Dosya.readline())

            Dosya.close()

    def read_lines():
        #--- "readlines()" belirtilen satırda okuma yapar, ve satırda yazılanları bir listeye alır
            Dosya = open("Erste Datei.txt", "r")

            print(Dosya.readlines()[2])

            Dosya.close()

    try:
        değer = int(input("\n drücken Sie 1 für modul_read. \n drücken Sie 2 für modul_readline.\n drücken Sie 3 modul_readlines.\n"))

        if değer == 1:
            read()

        elif değer == 2:
            read_line()

        elif değer == 3:
             read_lines()

        else:
            raise Exception("Sie dürfen nur 1, 2 oder 3 eingeben") #--- Sie dürfen keinen Wert größer als 3 oder kleiner als 1 eingeben.

    except Exception as Fehler:
        print("Sie hat einen Fehler gemacht", Fehler)




r_modul()