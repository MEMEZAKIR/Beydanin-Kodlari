
#ARGS VE KWARGS ÇALIŞ

import time

def Decorator1(func):
    def wrapper(x,y):
        başla = time.time()
        time.sleep(2)
        sonuç = func(x,y)
        bitir = time.time()
        süre = bitir-başla
        print(" sonuç: {}. programın çalışma süresi {}.".format(sonuç,süre))
    return wrapper 

@Decorator1
def çarpma(x,y):
    return x*y

@Decorator1
def toplama(x,y):
    return x+y

@Decorator1
def çıkarma(x,y):
    return x-y

@Decorator1
def bölme(x,y):
    return x/y

toplama(4,6)
çıkarma(15,10)
bölme(21,7)
çarpma(9,2)
