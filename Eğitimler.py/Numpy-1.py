import numpy as np

##-array = bir dizi oluşturur.
##-reshape = mevcut bir diziyi bir matrise çevirir.

def bişey1():
    dizi = np.array([1,2,3,4,5,6,7,8])
    dizi1 = np.array([[1,2],[3,4],[5,6],[7,8]]) #-matris.
    print(dizi)
    print(dizi1)
    print(dizi1.shape) #-kaça kaçlık bir matris olduğunu söyler.

def bişey2():
    dizi = np.array([1,2,3,4,5,6,7,8])
    dizi2 =dizi.reshape(4,2)
    dizi3 =dizi.reshape(2,4)
    print(dizi2)
    print(dizi3)

def dtype1():

   dizi4 = np.array([1,2,3,4,5,6,7,8]) #- int
   dizi5 = np.array(["1",2,3,"4",5,6,7,8]) #- <U11
   dizi6 = np.array([1.9,2,3.3,4,5,6.2,7,8]) #- float64

   print(dizi4.dtype)
   print(dizi5.dtype)
   print(dizi6.dtype)

dtype1()

    
    
