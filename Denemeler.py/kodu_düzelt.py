class game:
     def __init__(self,isim,silah,sınıf,):
        self.isim=isim
        self.silah=silah
        self.sınıf=sınıf  
        
x=game("{}","{}","{}".format(self.isim,self.silah,self.sınıf))
def oyun(self,isim,silah,sınıf,):
    seçim=int(input(print(""" oyuncu eklemek için [1] 
                      oyuncuları görüntülemek için [2]""")))

    
    if seçim==1:
            
                isim=input(print("karakterine bir isim ver"))
                silah_seçimi=int(input(print("""bir silah seç:
                                            balta için [1],
                                            kılıç için [2],
                                            mızrak için [3],
                                            hançer için [4]""")))
                if silah_seçimi==1:
                    silah="balta"
                elif silah_seçimi==2:
                    silah="kılıç"
                elif silah_seçimi==3:
                    silah="mızrak"
                elif silah_seçimi==4:
                    silah="hançer"
                else:
                    silah_seçimi=int(input(print("""tekrar dene!!!
                                                 bir silah seç:
                                                 balta için [1],
                                                 kılıç için [2],
                                                 mızrak için [3],
                                                 hançer için [4]""")))
            
                sınıf_seçimi=int(input(print("""bir sınıf seç
                                                şovalye için [1],
                                                hırsız için [2],""")))
        
                if sınıf_seçimi==1:
                    sınıf="şovalye"
                elif sınıf_seçimi==2:
                    sınıf="hırsız"
                else:
                    sınıf_seçimi=int(input(print(""" tekrar dene
                                                 bir sınıf seç
                                                şovalye için [1],
                                                hırsız için [2],""")))

                karakter=("{}({},{})\n".format(isim,sınıf,silah))

                karakterler.append(karakter)
                
                oyun()
                return  isim, sınıf, silah, x
    
    elif seçim==2:
        print(karakterler)
        oyun()