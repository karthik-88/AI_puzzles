maxA=int(input("enter capacity of A:"))
maxB=int(input("enter capacity of B:"))
waterinA=0
waterinB=0
targetA=int(input("enter target of container A:"))
targetB=int(input("enter target of container B:"))
while((waterinA != targetA or waterinB != targetB)):
    print("MENU\n1.fill A\n2.fill B\n3.empty A\n4.empty B\n5.A to B\n6.B to A\n")
    choice=int(input("enter your choice:"))
    if(choice == 1):
        waterinA=maxA
    elif(choice == 2):
        waterinB=maxB
    elif(choice == 3):
        waterinA=0
    elif(choice == 4):
        waterinB=0
    elif(choice == 5):
        if(waterinA<maxB):
            if(waterinA+waterinB<=maxB):
                temp=waterinA
                waterinB+=temp
                waterinA=0
        else:
            temp=maxB-waterinB
            waterinA-=temp
            waterinB+=temp
    elif(choice == 6):
        if((waterinA+waterinB<=maxB or waterinB-waterinA>0)):
            temp=waterinB
            waterinA+=temp
            waterinB=0
        else:
            temp1=maxA-waterinA
            waterinA+=temp1
            waterinB-=temp1
    print(waterinA,waterinB)
