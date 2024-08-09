def show(board,N):
    for i in range(N):
        for j in range(N):
            if board[i][j]==1:
                print("Q",end=" ")
            else:
                print("*",end=" ")
        print()
def position(board,r,c,N):
    for i in range(N):
        if(board[r][i]==1):
            return False
    for i in range(N):
        if(board[i][c]==1):
            return False
    for i in range(1,min(r,c)+1):
        if(board[r-i][c-i]==1):
            return False
    for i in range(1,min(r+1,N-c)):
        if(board[r-i][c+i]==1):
            return False
    for i in range(1,min(N-r,c+1)):
        if(board[r+i][c-i]==1):
            return False
    for i in range(1,min(N-r,N-c)):
        if(board[r+i][c+i]==1):
            return False
    return True
N=int(input("Enter the size of the board:"))
board=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    while True:
        row=int(input("enter the row position for queen: "))
        col = int(input("enter the column position for queen: "))
        if 0<=row<N and 0<=col<N:
            if position(board,row,col,N):
                board[row][col]=1
                show(board,N)
                break
            else:
                print("can't place")
        else:
            print("invalid position!!")
print("All positions are valid and the final board setup is: ")
show(board,N)
