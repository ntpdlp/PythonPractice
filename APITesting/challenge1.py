#Problem description
#Find out if there are any duplicate urls used in the
#json placeholder photo data

import requests

def main():

    url = 'https://jsonplaceholder.typicode.com/photos'

    #get the data about the photos
    response = requests.get(url)

    #read that data into a variable  
    json_data = response.json()

    #create a list for storing the url of each photo
    url_list = []
    for photo in json_data:
        #add the url for each photo to the url_list
        url_list.append(photo['url'])

    #How many items are in the url list (Should be 5000 since we have 5000 photos in our dataset)?
    print(len(url_list))

    #How many items are there if we turn that list into a set?
    url_set = set(url_list)
    print(len(url_set))

if __name__ == "__main__": main()