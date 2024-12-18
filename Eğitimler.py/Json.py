import json
# Dosyanın içeriği JSON formatında olmalı:
# Anahtar ve değer çiftleri arasında virgül olmalıdır.
# Anahtar isimleri ve değerler çift tırnak içinde olmalıdır.
# JSON formatında sayılar çift tırnak içinde olmamalıdır, doğrudan sayı olarak yazılmalıdır.

# JSON dosyasının doğru formatı şu şekilde olmalıdır:
# {
#     "isim": "Berdan",
#     "Soyad": "Bozan",
#     "Yas": 18
# }

def Dictionary():
    Bilgiler = {"Ad":"Beydan","Soyad":"Bojan","Mail":"beydan@gmail.com","Yas":18}

    print(Bilgiler["Ad"])


def Json_deneme():
    Bilgiler = """{"Ad":"Beydan","Soyad":"Bojan","Mail":"beydan@gmail.com","Yas":18}"""
   
    Bilgioku_json = json.loads(Bilgiler)

    print(Bilgioku_json,Bilgioku_json["Soyad"])


def Json_load():

    with open("C:/Users/user/Desktop/Beydanin kodları/birörnekişte.txt","r+", encoding="utf8") as Dosya:
       
        Bilgioku =json.load(Dosya)
       
        print(Bilgioku["Yas"])


def Json_dump():
    Bilgiler = {
    "isim": "Berdan",
    "Soyad": "Bozan",
    "Yas": 18
}
    #bilgioku=json.dumps(Bilgiler)

    with open("C:/Users/user/Desktop/Json_Ornekleri.txt","w+", encoding="utf8") as Dosya:
        json.dump(Bilgiler,Dosya)
        Dosya.seek(0)
        print(Dosya.read())

    with open("C:/Users/user/Desktop/Json_Ornekleri.txt","r+",encoding="utf8") as Dosya2:
        örnek = json.load(Dosya2)  
        print(örnek["Yas"])

Json_dump()