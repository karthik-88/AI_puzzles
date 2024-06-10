bank1S=3
bank1C=3
bank2S=0
bank2C=0
flag=0
while(1):
    if bank2S==bank2C==3:
        print("all cannibals and saints crossed river successfully!")
        exit(0)
    if (bank1C>bank1S):
        if((bank1C!=0)and(bank1S!=0)):
            print("cannibal eats saints!")
            exit(0)
    if (bank2C>bank2S):
        if((bank2C!=0)and(bank2S!=0)):
            print("cannibal eats saints!")
            exit(0)
    print("\n\n1.move 1 saint and 1 cannibal\n2.move 2 saints\n3.move 2 cannibals\n4.move 1 saint\n5.move 1 canibal")
    choice=int(input("enter your choice:"))
    if choice==1:
        if(flag==0):
            if((bank1C==0)or(bank1S==0)):
               print("input valid choice")
               continue
            print("boat in bank B")
            bank1C-=1
            bank2C+=1
            bank1S-=1
            bank2S+=1
            print("bank1:")
            print('S'*bank1S)
            print('C'*bank1C)
            print("bank2:")
            print('S'*bank2S)
            print('C'*bank2C)
            flag=1
        else:
            if((bank2C==0)or(bank2S==0)):
               print("input valid choice")
               continue
            print("boat in bank A")
            bank1C+=1
            bank2C-=1
            bank1S+=1
            bank2S-=1
            print("bank1:")
            print('S'*bank1S)
            print('C'*bank1C)
            print("bank2:")
            print('S'*bank2S)
            print('C'*bank2C)
            flag=0
    elif choice==2:
        if(flag==0):
            if(bank1S<2):
               print("input valid choice")
               continue
            print("boat in bank B")
            bank1S-=2
            bank2S+=2
            print("bank1:")
            print('S'*bank1S)
            print('C'*bank1C)
            print("bank2:")
            print('S'*bank2S)
            print('C'*bank2C)
            flag=1
        else:
            if(bank2S<2):
               print("input valid choice")
               continue
            print("boat in bank A")
            bank1S+=2
            bank2S-=2
            print("bank1:")
            print('S'*bank1S)
            print('C'*bank1C)
            print("bank2:")
            print('S'*bank2S)
            print('C'*bank2C)
            flag=0
    elif choice==3:
        if(flag==0):
            if(bank1C<2):
               print("input valid choice")
               continue
            print("boat in bank B")
            bank1C-=2
            bank2C+=2
            print("bank1:")
            print('S'*bank1S)
            print('C'*bank1C)
            print("bank2:")
            print('S'*bank2S)
            print('C'*bank2C)
            flag=1
        else:
            if(bank2C<2):
               print("input valid choice")
               continue
            print("boat in bank A")
            bank1C+=2
            bank2C-=2
            print("bank1:")
            print('S'*bank1S)
            print('C'*bank1C)
            print("bank2:")
            print('S'*bank2S)
            print('C'*bank2C)
            flag=0
    elif choice==4:
        if(flag==0):
            if(bank1S==0):
               print("input valid choice")
               continue
            print("boat in bank B")
            bank1S-=1
            bank2S+=1
            print("bank1:")
            print('S'*bank1S)
            print('C'*bank1C)
            print("bank2:")
            print('S'*bank2S)
            print('C'*bank2C)
            flag=1
        else:
            if(bank2S==0):
               print("input valid choice")
               continue
            print("boat in bank A")
            bank1S+=1
            bank2S-=1
            print("bank1:")
            print('S'*bank1S)
            print('C'*bank1C)
            print("bank2:")
            print('S'*bank2S)
            print('C'*bank2C)
            flag=0
    elif choice==5:
        if(flag==0):
            if(bank1C==0):
               print("input valid choice")
               continue
            print("boat in bank B")
            bank1C-=1
            bank2C+=1
            print("bank1:")
            print('S'*bank1S)
            print('C'*bank1C)
            print("bank2:")
            print('S'*bank2S)
            print('C'*bank2C)
            flag=1
        else:
            if(bank2C==0):
               print("input valid choice")
               continue
            print("boat in bank A")
            bank1C+=1
            bank2C-=1
            print("bank1:")
            print('S'*bank1S)
            print('C'*bank1C)
            print("bank2:")
            print('S'*bank2S)
            print('C'*bank2C)
            flag=0
    else:
        print("invalid choice")
