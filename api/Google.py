import requests
import json


def get(name="маленький принц"):
    try:
        in_book=name.replace(" ", "+")
        url = "https://www.googleapis.com/books/v1/volumes?q="+in_book
        #print(url)
        
        r=requests.get(url)
        
        return{ "title":r.json()['items'][0]['volumeInfo']["title"],
                "status":"found",
                "author":r.json()['items'][0]['volumeInfo']["authors"][0],
                'link':'not yet',
                "cover_link":r.json()['items'][0]['volumeInfo']["imageLinks"]["thumbnail"],
                "description":r.json()['items'][0]['volumeInfo']["description"],
                'review':'not yet'
                            }   
    except:
        return{ "title":name,
                "status":"not found"
            }   





if __name__ == "__main__":
    print(get("маленький принц"))