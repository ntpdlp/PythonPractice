def print_fibo(n):
    a,b = 0,1
    list = [a,b]
    while b<n:
        a,b = b,a+b
        list.append(b)
    for x in list:
        print(f"{x} " , end=' ', flush = True)  
    print("\r")

def sum_fibo(n):
    a,b = 0,1
    sum=a+b
    while b<n:
        a,b = b,a+b
        sum = sum + b
    return sum