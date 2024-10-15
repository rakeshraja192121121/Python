import random
list1=["rock","paper","scissor"]
user=int(input("Enter the choice:"))
if(user<0 or user>2):
    print("invalid")
else:
    print("user:",list1[user])
    computer=random.randint(0,2)
    print("computer choice :")
    print(list1[computer])
    if user==0 and computer==2:
        print("you won")
    elif user==2 and computer==0:
        print("you lose")
    elif(user > computer):
        print("user won")
    elif(user == computer):
        print("draw")
    else:
        print("computer won")
