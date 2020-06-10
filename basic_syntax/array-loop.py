#! /usr/bin/env python3

arr = [1,2,3,4,5,6,"One","Two"]
# for loop
for i in arr:
    print (f"{i}", end=' ')
print("\n")

for x in range(10):
    print(f"{x}",end=' ')
print("\n")

for y in range(50,70):
    if y%2 == 0:
        print(f"{y}",end=' ')
print("\n")

# while loop
n=0
while n<len(arr):
    print (f"{arr[n]}", end=' ')
    n = n+1
    pass
print("\n")    
