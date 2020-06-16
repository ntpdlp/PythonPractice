#! /usr/bin/env python2

import requests

def main():
    url = "https://api.github.com/user"
    #Authentication
    response = requests.get(url,auth=('djw-test','password1'))
    # #Token ID
    # response = requests.get(url,headers={'Authoriration':''})
    print(response.json())

if __name__ == "__main__":main()
