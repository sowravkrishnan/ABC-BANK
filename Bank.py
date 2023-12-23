import pickle
import os.path
import random
class Account:
    accNo = 0
    name = ''
    deposit = 0
    type = ''

    def createAccount(self):
        self.name = input("Enter the account holder name : ")
        self.type = input("Enter the type of account [C/S] : ")
        self.deposit = int(input("Enter The Initial amount"))
        self.accNo = random.randint(1001000, 1009999)
        print("\n\n\nAccount Created")
        print("Your account number is ",self.accNo)


def writeAccount():
        account = Account()
        account.createAccount()
        File(account)
def File(account):

    file = "bankdb"
    if os.path.isfile("bankdb"):
        infile = open("bankdb", "rb")
        old_data = pickle.load(infile)
        old_data.append(account)
        infile.close()
        os.remove("bankdb")
    else:
        old_data = [account]
    outfile = open('newbankdb', 'wb')
    pickle.dump(old_data, outfile)
    outfile.close()
    os.rename('newbankdb', 'bankdb')

def accountdetails():
    username = input("Enter your username:")
    accno = int(input("Enter account number: "))
    file="bankdb"
    if os.path.isfile("bankdb"):
        infile=open("bankdb","rb")
        data=pickle.load(infile)
        infile.close()
        for i in data:
            if i.name == username and i.accNo==accno:
                found=1
                print("Username =", i.name,"\n","Account number = ",i.accNo,"\n","Account type =",i.type, "\n","Balance = ",i.deposit)
                break
            else:
                found=0
                continue
        if found==0:
                print("Invalid credentials")

def modifydetails():
    username = input("Enter your username:")
    accno = int(input("Enter account number: "))
    file = "bankdb"
    if os.path.isfile("bankdb"):
        infile = open("bankdb", "rb")
        data = pickle.load(infile)
        infile.close()
        for i in data:
            if  i.name==username and i.accNo==accno:
                found=1
                i.name=input("Enter new username")
                i.type=input("Enter new account type(C/S)")
                break
            else:
                found=0
                continue
        if found==0:
            print("Invalid Credentials")
        os.remove("bankdb")
        outfile = open("newbankdb", "wb")
        pickle.dump(data,outfile)
        outfile.close()
        os.rename("newbankdb", "bankdb")
def creditamount():
    username = input("Enter your username:")
    accno = int(input("Enter account number: "))
    file = "bankdb"
    if os.path.isfile("bankdb"):
        infile = open("bankdb", "rb")
        data = pickle.load(infile)
        infile.close()
        for i in data:
            if i.name == username and i.accNo == accno:
                found = 1
                amount=int(input("Enter the amount"))
                i.deposit += amount
                print("Amount Deposited, Current balance=",i.deposit)
                break
            else:
                found = 0
                continue
        if found==0:
            print("Invalid Credentials")
        os.remove("bankdb")
        outfile = open("newbankdb", "wb")
        pickle.dump(data, outfile)
        outfile.close()
        os.rename("newbankdb", "bankdb")

def debitamount():
    username = input("Enter your username:")
    accno = int(input("Enter account number: "))
    file = "bankdb"
    if os.path.isfile("bankdb"):
        infile = open("bankdb", "rb")
        data = pickle.load(infile)
        infile.close()
        for i in data:
            if i.name == username and i.accNo == accno:
                found = 1
                amount=int(input("Enter the amount"))
                i.deposit -= amount
                print("Amount Debited, Current balance=",i.deposit)
                break
            else:
                found = 0
                continue
        if found==0:
            print("Invalid Credentials")
        os.remove("bankdb")
        outfile = open("newbankdb", "wb")
        pickle.dump(data, outfile)
        outfile.close()
        os.rename("newbankdb", "bankdb")

print("""
**********
*ABC BANK*
**********
1 CREATE ACCOUNT
2 ACCOUNT DETAILS
3 MODIFY ACCOUNT
4 DEPOSIT AMOUNT
5 WITHDRAW AMOUNT
""")

option = int(input("Enter your option:"))

if option==1:
    writeAccount()
elif option==2:
    accountdetails()
elif option==3:
    modifydetails()
elif option==4:
    creditamount()
elif option==5:
    debitamount()
else:
    print("Enter valid option")







