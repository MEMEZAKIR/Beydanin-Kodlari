import requests

#_Favori_Filmler
def bir():
    url = "https://api.themoviedb.org/3/account/{21673769}/favorite/tv"
    params = {
        "api_key": "79f37e110dd9ac7af705b449fb937f38",
        "session_id": "fd7faeb65aef93d35b3ecb10045e6dde6cacb6d9"
    }

    response = requests.get(url, params=params)
    data = response.json()

    print(data)  # Favori dizilerin listesi

#_Film_IDleri
def iki():
    secim = input("1 ya da 2: ")
    def ikinin_biri():
        movie_name = "Inception"  # Kullanıcıdan alınan film adı
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": "79f37e110dd9ac7af705b449fb937f38",
            "query": movie_name
        }

        response = requests.get(url, params=params)
        data = response.json()
        print(data)

    def ikinin_ikisi():
        movie_name = "Inception"  # Kullanıcıdan alınan film adı
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": "79f37e110dd9ac7af705b449fb937f38",
            "query": movie_name
        }

        response = requests.get(url, params=params)
        data = response.json()

        # İlk sonucu alalım
        if data["results"]:
            first_result = data["results"][0]
            movie_id = first_result["id"]
            print(f"Film Adı: {first_result['title']}, ID: {movie_id}")
        else:
            print("Film bulunamadı.")

    if secim == "1":
        ikinin_biri()
    elif secim == "2":
        ikinin_ikisi()

#_Filmi_Favorilere_ekleme
def üç():
    url = "https://api.themoviedb.org/3/account/{account_id}/favorite"
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "api_key": "79f37e110dd9ac7af705b449fb937f38",
        "session_id": "fd7faeb65aef93d35b3ecb10045e6dde6cacb6d9"
    }
    raw_body = {
        "media_type": "tv",       # tv ya da movie seçebilirsiniz
        "media_id": 12345,        # Favoriye eklemek istediğiniz içerik ID'si
        "favorite": True
    }

    response = requests.post(url.format(account_id=21673769), headers=headers, params=params, json=raw_body)
    
    durum = response.json()

    if durum['status_message'] == 'Success.':
        print("Favorilere eklendi")
    else:
        print("Bir hata oluştu")

    print(response.json())

def dört():
    url = "https://api.themoviedb.org/3/movie/popular"
    params = {
        "api_key": "79f37e110dd9ac7af705b449fb937f38",  # Sizin API key'iniz
        "language": "en-US",  # İstediğiniz dil
        "page": 2  # İlk sayfa
    }

    response = requests.get(url, params=params)
    print(response.json())

dört()
