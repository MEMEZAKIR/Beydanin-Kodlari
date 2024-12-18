class Müşteri:
    def __init__(self,isim,TC,şifre,bakiye,borç,sonödeme,borç_al):
        self.isim=isim
        self.TC=TC
        self.şifre=şifre
        self.bakiye=bakiye
        self.borç=borç
        self.sonödeme=sonödeme
        self.borç__al=borç_al

Mehmet_bey=Müşteri("Mehmet Çakır","12345678911","12345",15000,0,"22.12.24",0) 
Ajda_hanım=Müşteri("Ajda Gulufulu","11987654321","vututututu",45000,0,"23.03.24",0)

print("mehmey beyin kartını takmak için 1 Ajda hanımın kartını takmak için 2ye basınız.")

kart=input()
if (kart=="1"):
    x=Mehmet_bey

elif (kart=="2"):
    x=Ajda_hanım

Takılan_kart=x

class ATM:
    def __init__(self,):
        self.giriskontrol()
        self.döngü=True
    
    def giriskontrol(self):
        giris_hakkı=3
        for i in range(0,3):
            Şifre=input("Şifrenizi giriniz.")
            if Şifre==Takılan_kart.şifre:
                print("hg")
                self.program()
                break
                
            elif Şifre!=Takılan_kart and giris_hakkı!=1:
                giris_hakkı-=1
                print("şifreyi yanlış girdin. Kalan haıkkın {}".format(giris_hakkı))
            
            elif Şifre!=Takılan_kart and giris_hakkı==1:
                print("hakkın kalmadı bb")
                exit()
    

    def menu(self):
        talep=input(""" 
        bakiye sorgulama için (1)
        kredi kartı borcu sorgulama için (2) 
        para çekme için (3)
        para yatırma için (4)
        son ödeme tarihi sorgulaması için (5)
        borç almak için (6)
        çıkmak için (Q)""")

        return talep

    def program(self):
        talep = self.menu()


        if talep=="1":
            self.bakiye()
        elif talep=="2":
            self.borç()
        elif talep=="3":
            self.çekim()
        elif talep=="4":
            self.yatır()
        elif talep=="5":
            self.son_ödeme_tarihi()
        elif talep=="6":
            self.borç_al()
        elif talep=="Q":
            self.döngü=False
            exit()  




    def bakiye(self):
        if Takılan_kart.bakiye>=100000:
            print("\n\n\n{} TL var. \n\n\n".format(Takılan_kart.bakiye))
        elif Takılan_kart.bakiye<=5000 and Takılan_kart.bakiye>=1:
            print("\n\n\n{} TL var.  fakir \n\n\n".format(Takılan_kart.bakiye))
        elif Takılan_kart.bakiye<=-1:
            print("\n\n\n{} TL borcun var.  ÖDESENE".format(Takılan_kart.bakiye))
        elif Takılan_kart.bakiye==0:
            print("QSAEWDWEADRFGAYHUIDABDASFASTVFYASTVF FAKİR:D FAKİRASBYUFUANIGMAGSYAUGSNIMOGSAGYBAUISGNOIMKASLGÆßGASGNKQLGQSYAUGSNIMOGSAGYBAUISGNOIMKASLG´ÆßGASGNKQLGQSYAUGSNIMOGSAGYBAUISGNOIMKASLG´ÆßGASGNKQLGQSYAUGSNIMOGSAGYBAUISGNOIMKASLG´ÆßGASGNKQLGQSYAUGSNIMOGSAGYBAUISGNOIMKASLG´ÆßGASGNKQLGQSYAUGSNIMOGSAGYBAUISGNOIMKASLG´ÆßGASGNKQLGQ  ALLAHIN FAKİRİ ZUHAHAHHAHAHAHHAHAHAHAHAHAHAHAHHAHAHAHHAHAHAHAHAHHAHA ZUHAHAHHAHAHAHHAHAHAHAHAHAHAHAHHAHAHAHHAHAHAHAHAHHAHA ZUHAHAHHAHAHAHHAHAHAHAHAHAHAHAHHAHAHAHHAHAHAHAHAHHAHA ZUHAHAHHAHAHAHHAHAHAHAHAHAHAHAHHAHAHAHHAHAHAHAHAHHAHA ZUHAHAHHAHAHAHHAHAHAHAHAHAHAHAHHAHAHAHHAHAHAHAHAHHAHA ZUHAHAHHAHAHAHHAHAHAHAHAHAHAHAHHAHAHAHHAHAHAHAHAHHAHA ZUHAHAHHAHAHAHHAHAHAHAHAHAHAHAHHAHAHAHHAHAHAHAHAHHAHA ZUHAHAHHAHAHAHHAHAHAHAHAHAHAHAHHAHAHAHHAHAHAHAHAHHAHA")
        else:
            print("\n\n\n{} TL var. \n\n\n".format(Takılan_kart.bakiye))
        self.program()

    def borç(self):
        if Takılan_kart.bakiye<=-100000:
            print("\n\n\n{} TL...  bok ödersin bu borcu :D\n\n\n".format(Takılan_kart.bakiye))
        elif Takılan_kart.bakiye<=-1 and Takılan_kart.bakiye>=-100000:
            print("\n\n\n{} TL borcun var, PARAMI VER \n\n\n".format(Takılan_kart.bakiye))
        else:
            print("\n\n\nborcun yok, şimdikik...\n\n\n")

        self.program()

    def çekim(self):
        çekilecek_miktar=int(input())
        if çekilecek_miktar>Takılan_kart.bakiye:
            print("\n\n\n\n git babandan iste {} TL yi \n\n\n\n".format(çekilecek_miktar))
            self.program()
        else:
            Yeni_bakiye=Takılan_kart.bakiye-çekilecek_miktar
            Takılan_kart.bakiye=Yeni_bakiye
            print("\n\n\nHesabında {} TL kaldı,\n\n\n".format(Yeni_bakiye))
            self.program()


    def yatır(self):
        yatırılacak_miktar=int(input())
        Yeni_bakiye=Takılan_kart.bakiye+yatırılacak_miktar
        Takılan_kart.bakiye=Yeni_bakiye
        print("\n\n\n Hayret para almadın bu sefer \n\n bakiyen {} TL oldu bu arada \n\n\n".format(Takılan_kart.bakiye))
        self.program()

    def son_ödeme_tarihi(self):
        print(Takılan_kart.sonödeme)
        self.program()
    

    def borç_al(self):
        borç_miktarı=int(input())
        Yeni_bakiye=Takılan_kart.bakiye-borç_miktarı
        Takılan_kart.bakiye=Yeni_bakiye
        print("\n\n\n{} TL borç aldınız. yeni bakiyeniz{}TL\n\n\n".format(borç_miktarı,Takılan_kart.bakiye))
        self.program()

Banka=ATM()
while Banka.döngü:
    Banka.program()