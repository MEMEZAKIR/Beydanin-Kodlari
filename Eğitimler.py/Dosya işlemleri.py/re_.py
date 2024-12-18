
import re

#---Aranılan değer aranılan yerde ise bir Liste oluşturur(değilse boş bir liste dödürür)

def findall_çalısss(): 
    x = "Hallo, Ich heiße Beydan"
    y = re.findall("Hallo", x)
    z = re.findall("etwas, das nicht existiert", x)
    q = re.findall("[a-g]", x)
    ş = re.findall("[^a-g]", x)
    a = re.findall("^H", x)
    b = re.findall("^b", x)
    c = re.findall(".$", x)
    print( y, z, q, ş, a, b, c)

#---Bir Stringden belirtilen değerlerden arındırır

def split1():
    x = "Meine Lieblingsmusikgruppe ist Ramstein"
    y = re.split(" ", x)
    print(y)

def split2():
    x = "Meine Lieblingsmusikgruppe ist Ramstein"
    y = re.split("e", x)
    print(y)

#---Belirtilen değeri yenisiyle değiştirir

def sub1():
    x = "Küfür etme aq"
    y = re.sub("aq","*",x)
    print(y)

def sub2():
    x = "Berdan Borasını düşürdü"
    y = re.sub("r","y",x)
    print(y)

#---Bazı özellikleri fln var. span ve match

def search1():
    x = "Howdy, you alright mate"
    y = re.search("Howdy", x)
    z = re.search("[p-z]", x) #--ilk bulduğunu yazdırır
    print(y.span()) #--karakterin nerede başlayıp bittiğini gösterir.
    print(y.start()) #--karakterin nerede başladığını gösterir.
    print(y.end()) #--karakterin nerede bittiğini gösterir.
    print(y.string)#-- karakteri nerede aradığını gösterir.
    print(z)


def findall_deneme():
    x = "deneme yapma vakti, hadi başlayalım"
    y = re.findall("[n-z]", x)
    z = re.findall("[^n-z]", x)
    q = re.findall("^d", x) #--girilen değerin istenilen string dizisindeki ilk değer olup olmadığını kontrol eder; 
                            #--evet ise, içinde değerin olduğu bir liste oluşturur. hayır ise boş bir liste döndürür.

    a = re.findall("^g", x)
    b = re.findall("m$", x)
    c = re.findall("a$", x)

    print(y, z, q, a, b, c)
search1()

