import requests
import json
import time
import re
import textwrap

#{"success":True,"session_id":"fd7faeb65aef93d35b3ecb10045e6dde6cacb6d9"}
#{"success":True,"expires_at":"2024-12-07 01:21:12 UTC","request_token":"6e89e3bc06753bc48fbb4acb041c4ce70c441265"}
#API_key = "79f37e110dd9ac7af705b449fb937f38"
#API_Read_Access_Token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3OWYzN2UxMTBkZDlhYzdhZjcwNWI0NDlmYjkzN2YzOCIsIm5iZiI6MTczMzUwODIzNy45MjUsInN1YiI6IjY3NTMzYzhkNTE2ZWRlYWIyOTk5NGU5NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.vn8i4bHGCgJptXCRcb1nl9SX8kWaRpe1oLsp_2eVNKk"
#account_id = 21673769

class Kullanıcı:
    def __init__(self, account_id, API_key, session_id, API_Read_Access_Token):
        self.dongu = True
        self.account_id = account_id
        self.API_key = API_key
        self.session_id = session_id
        self.API_Read_Acces_Token = API_Read_Access_Token

kullanıcı = Kullanıcı(
    account_id="21673769",
    API_key="79f37e110dd9ac7af705b449fb937f38",
    session_id="fd7faeb65aef93d35b3ecb10045e6dde6cacb6d9",
    API_Read_Access_Token="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3OWYzN2UxMTBkZDlhYzdhZjcwNWI0NDlmYjkzN2YzOCIsIm5iZiI6MTczMzUwODIzNy45MjUsInN1YiI6IjY3NTMzYzhkNTE2ZWRlYWIyOTk5NGU5NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.vn8i4bHGCgJptXCRcb1nl9SX8kWaRpe1oLsp_2eVNKk"
)

class Film:
    def __init__(self,kullanıcı):
        self.dongu = True 
        self.kullanıcı = kullanıcı

    def time(self, x):
        for i in range(x):
            print(".",end="",flush=True)
            time.sleep(.5)
        time.sleep(.6)
         


    def menu(self):
        def control(secim):
            if secim.isdigit() == False:
                raise Exception("\nYou cannot enter any value other than numbers!")
            elif re.search("[^1-5]",secim):
                raise Exception("\nPlease enter a value between 1 and 5!")
            elif len(secim) != 1:
                raise Exception("\nPlease enter a value between 1 and 5!")

        while True:    
            try:
                secim = input("""
                        \nWelcome.
                            [1]- Popular Movies
                            [2]- Popular TV Series
                            [3]- My Favorities
                            [4]- Add to my favorities
                            [5]- Exit
                              """)
                control(secim)
            except Exception as Hata:
                print(Hata)
                time.sleep(2)
            else:
                break
        return secim
        
    def program(self):
        secim = self.menu()

        if secim == "1":
            self.time(3)
            self.popular_movies(page = 1)

        elif secim == "2":
            self.time(3)
            self.popular_tv_series(page = 1)
        
        elif secim == "3":
            self.time(3)
            self.my_favorites()

        elif secim == "4":
            self.time(3)
            self.add_to_my_favorities()

        elif secim == "5":
            self.time(3)
            self.exit()

    
    def popular_movies(self,page):
        while True:
            
            if page is None:
                page = 1

            url = "https://api.themoviedb.org/3/movie/popular"
            
            params = {
                "api_key": kullanıcı.API_key,  
                "language": "en-US",  
                "page": page  # İlk sayfa
            }

            response = requests.get(url, params=params)
            data = response.json().get("results")
            print("\nPopular Movies:")

            for movies in data:
                print(f'-{movies["title"]}- ({movies["release_date"]}), Ratings: {movies["vote_average"]}')
            
            while True:
                secim = input(f"\n Page: {page}\n\n [1]- Choosing a page number:\n [2]- back to menu:\n [3]- exit:")
                if secim == "1":
                    new_page = int(self.page_number())
                    page = new_page
                    break
                
                elif secim == "2":
                    return

                elif secim == "3":
                    self.exit()
                    break
                    

                elif secim not in ["1", "2", "3"]:
                    print("Invalid selection, please try again.")



    def popular_tv_series(self,page):
       while True:
            
            if page is None:
                page = 1

            url = "https://api.themoviedb.org/3/tv/popular"
            
            params = {
                "api_key": kullanıcı.API_key,  
                "language": "en-US",  
                "page": page  # İlk sayfa
            }

            response = requests.get(url, params=params)
            data = response.json().get("results")
            print("\nPopular TV Series")
            for series in data:
                print(f'-{series["name"]}- ({series["first_air_date"]}), Ratings: {series["vote_average"]}')
            
            while True:
                secim = input(f"\n Page: {page}\n\n [1]- Choosing a page number:\n [2]- back to menu:\n [3]- exit:")
                if secim == "1":
                    new_page = int(self.page_number())
                    page = new_page
                    break
                
                elif secim == "2":
                    return

                elif secim == "3":
                    self.exit()
                    break
                    

                elif secim not in ["1", "2", "3"]:
                    print("Invalid selection, please try again.")
    
    def add_to_my_favorities(self,):
        while True:
            url = f"https://api.themoviedb.org/3/account/{self.account_id}/favorite??session_id={self.session_id}"
            
            payload = {
            "media_type": media_type,
            "media_id": media_id,
            "favorite": favorite
            }


    def my_favorites(self):
        pass

    def search(self):
        pass

    def directly_addtomyfrts(self):
        pass

    def page_number(self):
        while True:
            page = input("Enter the page you want to see:")
            if page.isdigit() and 1 <= int(page) <= 10:
                return int(page)  # Düzgün bir sayı girildi, dönüş yapılabilir
            else:
                print("You can only enter a number between 1 and 10")
        

    def exit(self):
        print("BYEEEEEEE")
        time.sleep(2)
        exit()

Sistem = Film(kullanıcı)
while Sistem.dongu:
    Sistem.program()