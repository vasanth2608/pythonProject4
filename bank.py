#Banking application

def CreateAccounts():
     AccountNo = int(input("enter account Number"))
     CustomerName = input("enter name")
     BranchCode = input("enter branch Code")
     MobileNo = int(input("enter mobile number"))
     Balance = int(input("enter current Balance"))

def ShowAccountDetails():
    print("AccountNo:",Accountno)
    print("CustomerName:",CustomerName)
    print("BranchCode:",BranchCode)
    print("MobileNo:",MobileNo)

def Deposit(amount):
    Bal = Bal+amount
    checkbalance()

def Withdraw(amount):
    Bal = Bal-amount
    checkbalance()

def checkbalance():
    print("current Balance:",Balance)
choice1='y'
while(choice1=='y'):
    print("1.Create account\n 2.Withdraw\n 3.deposit\n 4.checkbalance\n")
    choice=int(input("select any option"))
    if(choice==1):
       CreateAccounts()
    elif(choice==2):
       amt=int(input("enter amount to withdraw"))
       withdraw(amount)
    elif(choice==3):
       amount=int(input("enter amount to deposit"))
       deposit(amount)
    elif(choice==4):
      checkbalance()
    else:
      print("please select any 4 option available above")
    print("do you want to continue..press y")
    choice1=input()
