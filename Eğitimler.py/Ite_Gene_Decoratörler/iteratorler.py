# iterator'ler gezgindir. Bir objeye gider ve o objenin elemanlarını donanır.

def for_ornegi():
    Liste = [1,2,3,4,5]
    for i in Liste:
        print(i)

def iterator_erklärung():
    Liste = [1,2,3,4,5]

    Iterator = iter(Liste) #Bir iteratör oluştururuz ve Liste'yi o iteratörün içerisine ekleriz, sonrada Iteratör değererine atadık.

    değer = next(Iterator) #Seçilen iteratör değeri üzerinde(Iterator) gezinir. burada 1'i seçer ve değer yapısına atar 
    
    değer_2 = next(Iterator) #Burada ise sonraki değere yani 2'ye geçer sonrasında onu değer 2'ye atarız
    
    print(değer)
    print(değer)
    print(değer_2)

    print(next(Iterator)) # istersek hiçbir değer girmeyiz ve next fonksiyonu otomatik olarak her seferinde sonraki değere ilerler
    print(next(Iterator))

def iterator():
    Liste=[1,2,3,4,5]
    Iterator=iter(Liste)
    while True:
        try:
            tara = next(Iterator)
            print(tara)
        
        except StopAsyncIteration:
            break

def Iterator_tam_ornek():

    class Sayılar:
        def __init__(self,başlangıç,bitiş):
            self.başlangıç=başlangıç
            self.bitiş=bitiş

        def __iter__(self):
            return self

        def __next__(self):
            if self.başlangıç<=self.bitiş:
                x = self.başlangıç
                self.başlangıç+=1
                return x
            else:
                raise StopAsyncIteration
            

    for i in Sayılar(1,100):
        print(i)

iterator_erklärung()