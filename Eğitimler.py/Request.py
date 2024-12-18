import requests
import time
import json

def response(): #Wenn die response 200 ist, bedeutet das, dass der Zugriff erlaubt ist
                #If the response is 200, it means access is granted.
    site = requests.get("https://jsonplaceholder.typicode.com/todos")

    print(site)



def type_example_str(): #Bir siteden gelen değerler ilk başta str halindedir
    site = requests.get("https://jsonplaceholder.typicode.com/todos")
    antwort = site.text

    print(type(antwort))



def type_example_list(): #Gelen bilgiler json formatında ise,
                         #Onları json yapısına çevirebilir,
                         #Bunun sonucunda yeni bilgilerimizin sınıfı List olucaktır

    site = requests.get("https://jsonplaceholder.typicode.com/todos")
    antwort = json.loads(site.text)

    print(type(antwort))

def json_example(): #Bilgiler artık koca bir liste
    site = requests.get("https://jsonplaceholder.typicode.com/todos")
    antwort = json.loads(site.text)

    print(antwort)


def json_example_0(): #Bir Listenin elemanlarının "Hücre" diye adlandırıldığını varsayalım
    site = requests.get("https://jsonplaceholder.typicode.com/todos")
    antwort = json.loads(site.text)

    for i in antwort: #Bu şekilde Listemizin içerisindeki bütün Hücreleri yazdırabiliriz
        print(i)

def json_example_1():
    site = requests.get("https://jsonplaceholder.typicode.com/todos")
    antwort = json.loads(site.text)

    print(antwort[0]) #İlk değer listenin ilk hücresidir
    time.sleep(2)
    print(antwort[0]["title"]) #Bir hücrenin farklı elemanlarını bu şekilde çekebiliriz
    time.sleep(2)
    print(antwort[0]["userId"])



def json_example_2(): # Bütün hücrelerdeki "title" değerlerini döndürür
    site = requests.get("https://jsonplaceholder.typicode.com/todos")
    antwort = json.loads(site.text)
    for i in antwort:
        print(i["title"])
        
json_example_2()