def myHelloFunction():
    print ("this is my sub-function")
myHelloFunction()


def checkBalance(inbank):
    if (inbank < 10):
        print ("your amount < $10")
    else:
        print ("good amount >= $10")
checkBalance(5)


def withdrawFromAccount(current_account, amount):
    if (current_account > amount):
        current_account = current_account - amount
        print ("remaining $ in your account: ", current_account)
        return current_account
    else:
        print ("you are withdrawing over your amount in your account")
new_balance = withdrawFromAccount(500,50)

str = "I am very passionate about software quality."
print(len(str))
