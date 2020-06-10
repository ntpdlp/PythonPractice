#! /usr/bin/env python3


def withdrawFromAccount(current_account, amount):
    if (current_account > amount):
        current_account = current_account - amount
        return current_account
    else:
        print ("Fail")


def function_default_arguments(a,b,c):
    print (f"a is {a}, b is {b}, c is {c}")

def main():
    new_balance = withdrawFromAccount(500,50)
    print (f"New balance is: {new_balance}")
    print (f"New balance is: {withdrawFromAccount(500,50)}")

    function_default_arguments(1,2)


if __name__ == "__main__": main()