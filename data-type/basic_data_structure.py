#! /usr/bin/env python3

print("List",end="\t")
list = [1,2,3,4,5]
for x in list:
    print(f"{x} ", end=' ')

print("Tuple", end="\t")
tuple = (6,7,8,9)
for x in tuple:
    print(f"{x} ",end=' ')

print("Set", end="\t")
set = {11,12,15,17}
for x in set:
    print(f"{x} ",end=' ')

print("Dictionary", end="\t")
dic = dict(one=1, two=2, three=3)
for k in dic:
    print("{}:{} ".format(k,dic[k]),end=' ')

