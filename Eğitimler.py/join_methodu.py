import re

#--Boşlukla Birleştirme:
words = ["Merhaba", "dünya"]
sentence = " ".join(words)
print(sentence)  # Çıktı: "Merhaba dünya"



#--Virgülle Birleştirme:
items = ["elma", "armut", "kiraz"]
fruits = ", ".join(items)
print(fruits)  # Çıktı: "elma, armut, kiraz"



#--Hiçbir Şeyle Ayırmadan Birleştirme:
characters = ["a", "b", "c"]
joined = "".join(characters)
print(joined)  # Çıktı: "abc"



    #---join metodu, bir iterable (tekrarlanabilir) nesnedeki öğeleri birleştirerek tek bir string oluşturur.
    #---Python'da str sınıfının bir metodudur ve özellikle listelerdeki string öğeleri birleştirmek için kullanılır.



Liste = ["z", "c", "d"]
if "g" not in Liste:
    print("aaaaaaa")

z = re.findall("d", "".join(Liste))  # Join list elements into a single string
if "d" in z:
    print("d var")
else:
    print("d yok")

z = re.findall("y", "".join(Liste))  # Join list elements into a single string
if "y" in z:
    print("y var")
else:
    print("y yok")


    #---join metodu, bir iterable (tekrarlanabilir) nesnedeki öğeleri birleştirerek tek bir string oluşturur.
    #---Python'da str sınıfının bir metodudur ve özellikle listelerdeki string öğeleri birleştirmek için kullanılır.
