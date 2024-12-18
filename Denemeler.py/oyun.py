import random

class oyuncu:
    def __init__(self,isimi,sırası):
        self.isimi=isimi
        self.sırası=sırası
    
    #def yenioyuncu_ekleme(self):
        sayı=int(input())
        range(1,sayı)
        self.isimi=input("isminizi giriniz")
        self.sırası=0
        self.ismi=oyuncu(self.isimi,0)
        return
         


SIRA=[]
x=0

for i in range(0,101):
    SIRA.append(i)
for i in range(4,100,23):
    SIRA[i]=i



for i in range(0,25):
    başlat=int(input("0 yaz"))
    if başlat==0:
        zar=random.randint(1,6)
        x=SIRA[x+zar]
        yeni_sıra=x      
        print("puanın",yeni_sıra)
