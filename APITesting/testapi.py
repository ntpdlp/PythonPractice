#! /usr/bin/env python

#press : Shift + Command + P >> Python Interpreter >> 2.7
import requests


def api_get():
    url = "https://jsonplaceholder.typicode.com/photos/5"
    response = requests.get(url)
    print(response.json())
    print("check Id: {}".format(response.json()['id']))

    url2 = "https://jsonplaceholder.typicode.com/photos"
    response2 = requests.get(url2)
    curTotal = len(response2.json())
    print(curTotal)

def api_post_put():
    url3 = "https://jsonplaceholder.typicode.com/photos"
    apayload = {'url': 'new post photo', 
                'albumId': 1, 
                'thumbnailUrl': 'new post photo', 
                'title': 'new post photo'
                }
    response3 = requests.post(url3,json=apayload)
    print(response3.json())

    url4 = "https://jsonplaceholder.typicode.com/photos/100"
    response4 = requests.put(url4,json=apayload)
    print(response4.json())

def main():
    # api_get()
    api_post_put()




if __name__ == "__main__":main()
    