#! /usr/bin/env python3

import datetime
def func_datetime():
    print(datetime.datetime.today())
    print(datetime.datetime.now())
    dnow = datetime.datetime.now()
    print(dnow.year)
    print("{}/{}/{} : {}:{}:{}".format(dnow.year, dnow.month, dnow.day, dnow.hour, dnow.minute, dnow.second))
    
    # print(datetime.datetime.year())
    # print(datetime.datetime.month())

def main():
    func_datetime()

if __name__ == "__main__":main()