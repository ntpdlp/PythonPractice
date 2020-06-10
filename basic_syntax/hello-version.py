#! /usr/bin/env python3

import platform
platformstr = platform.python_version()
print ("Python version {}".format(platformstr))

num = 50
name = "Phuong"
print ("your $$ is: %d" %num) #python2, legacy code style
print ("your $$ is: {}".format(num)) #python3
print ("{} has money {}".format(name,num))
print (f"Your $$ is: {num}") #python3
print (f"{name} has money {num}")
