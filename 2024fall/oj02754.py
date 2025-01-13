def check(board,row,col):
    for i in range(row):
        if board[i]==col or board[i]-i==col-row or board[i]+i==col+row:
            return False
    return True

def queens_8(row,board,result):
    if row==8:
        result.append(board[:])
        return
    for col in range(1,9):
        if check(board,row,col):
            board[row]=col
            queens_8(row+1,board,result)
    return result

T=int(input())
answers=[]
result=[]
board=[-1]*8
solution=queens_8(0,board,result)
for _ in range(T):
    i=int(input())
    answers.append(solution[i-1])
for answer in answers:
    for s in answer:
        print(s,end='')
    if answer!=answers[-1]:
        print()