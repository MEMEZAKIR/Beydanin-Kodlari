def araba(**kwargs):
    for key,value in kwargs.items():
        if value>250000:
            print("{} pahalı".format(key))
        else:
            print("{} ucuz".format(key))


araba(Mercedes=290000,Ferrari=100000000,fiat=1, Audi=260000,renault=2)



















#def ortalama(*args,x):
    #toplam=0
   # for i in args:
  #      toplam = toplam + i
    
 #   ortalama = (toplam / len(args))
    
#    if ortalama>x:
  #      print(" ortalamadan küçük")
   # else:
    #    print(" ortalamadan büyük ")

 #   return round(ortalama,3)

#ortalama(60,100,124,87,57,x=87)
