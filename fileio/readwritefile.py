#! /usr/bin/env python3

import os

def workwithtextfile():
    pwd = os.path.dirname(os.getcwd())
    f = open(pwd + "/fileio/textinputsample.txt","rt") #read text
    fopen = open(pwd + "/fileio/textoutputsample.txt","wt") #write text
    for line in f:
        #print(line.rstrip(), file=fopen)  #way1 to write file
        fopen.writelines(line)             #way2 to write file
        print (" .",end=" " , flush=True) #showing progress ...
    print("\ndone")
    fopen.close()
    f.close()

def workwithbinaryfile():
    pwd = os.path.dirname(os.getcwd())
    f = open(pwd + "/fileio/binaryinputsample.jpg","rb") #read binary
    fsizeint = os.path.getsize(pwd + "/fileio/binaryinputsample.jpg")
    print(f"File size in bytes: {fsizeint}")
    fopen = open(pwd + "/fileio/binaryoutputsample.jpg","wb") #write binary
    buf = f.read(10240)
    while buf:    
        fopen.write(buf)
        print (" .",end=" " , flush=True) #showing progress ...
        buf = f.read(10240)
    print("\ndone")
    fopen.close()
    f.close()



def main():
    workwithtextfile()
    workwithbinaryfile()

if __name__ == "__main__": main()