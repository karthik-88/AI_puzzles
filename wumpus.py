import numpy as np
place=np.array([['_','_','_','_'],
                ['_','_','_','_'],
                ['_','_','_','_'],
                ['_','_','_','_']])
wrong=np.array([['s','_','b','p'],
                ['w','s','p','b'],
                ['s','_','b','_'],
                ['_','b','p','b']])
gold=[1,1]
i=3
j=0
while True:
    place[i][j]='p'
    print(place)
    print(" U ")
    print("L R")
    print(" D ")
    choice=input("enter next move:(U/L/R/D):")
    match choice:
        case 'U':
            if(i!=0):
                place[i][j]='O'
                i-=1
        case 'L':
            if(j!=0):
                place[i][j]='O'
                j-=1
        case 'R':
            if(j!=3):
                place[i][j]='O'
                j+=1
        case 'D':
            if(i!=3):
                place[i][j]='O'
                i+=1
    if(gold==[i,j]):
        print("u won!!!")
        break
    elif(wrong[i][j]=="w"):
        print("wumpus ate you!")
        break
    elif(wrong[i][j]=="p"):
        print("you fell into pit!")
        break
    elif(wrong[i][j]=="s"):
        print("wumpus around you!")
    elif(wrong[i][j]=="b"):
        print("pit around you!")
