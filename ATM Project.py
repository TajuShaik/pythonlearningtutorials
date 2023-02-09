#ATM Project
print("*"*15," Welcome to SBI Bank ATM",15*"*")
while True:
    lan = input("Enter  your language:(Eng)")
    if lan=='Eng' or "English":
        if lan.isalpha():
            break
    else:
        print("Invalid Please enter your language Ex:Eng or English")
while True:
    name= input("Enter  your Name:")
    if name.isalpha():
        break
    else:
        print("Invalid Please enter your Name")
while True:
    pin = (input("Enter your Four digit Pin:"))
    pinl = len(pin)
    if pinl == 4:
        break
    else:
        print("Incorrect pin please enter four digits pin")
while True:
    print("Choose Your Account type: 1)Savings 2)Current ")
    Acc_type =input("Enter option 1 or 2:")
    if Acc_type ==1 or 2:
        break
#print(" Please Choose 1 or 2 as per your Bank Account type like 1)savings or 2)current")
while True:
    print("*"*15,"Choose your choice from below Operations",15*"*")
    print("\t1.Balance Enquiry")
    print("\t2.Withdrawal")
    print("\t3.Deposit")
    print("\t4.Exit")
    ch=int(input("Enter  your  Choice:"))
    if ch>=1 and ch<=4:
        break
    else:
        print("Incorrect input please choose valid option")
a=20000
match ch:
        case 1:
             print("Balance is ",a)
        case 2:
             w=int(input("Enter Withdrawal Amount:"))
             print("remaining balance amount is :",a-w)
        case 3:
             D=int(input("Enter Deposit Amount : "))
             print("Dposit Succesful balance is:",D+a)
        case 4:
             print("exit")

















