class Atm(object):
    def __init__(self,pinNumber,cardNumber):
        self.pinNumber = pinNumber
        self.cardNumber = cardNumber
    def checkBalance(self):
        print("Rs.50,000")
    def withdrawl(self,amount):
        newamount = 50000-amount
        print("You Have Withdrawl Amount"+str(amount)+"Your Remaining Balance Is"+str(newamount))
def main():
    cardNumber = input("Insert Your Card Number")
    pinNumber = input("Insert Your Pin Number")
    new_user = Atm(cardNumber,pinNumber)
    print("Choose Your Activity")
    print("1.Bank Inquiry 2.Withdrawl")
    activity = int(input("Enter Activity Number"))
    if (activity == 1):
        new_user.checkBalance()
    elif (activity == 2):
        amount = int(input("Enter The Amount"))
        new_user.withdrawl(amount)
    else:
        print("Enter A Valid Number")
main()
