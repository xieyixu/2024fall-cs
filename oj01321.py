def backtrack(board,n,k,row,cols,count):
    if k==0:
        count[0]+=1
        return
    if row>=n:
        return

    for col in range(n):
        if board[row][col]=='#' and not cols[col]:
            cols[col]=-1
            backtrack(board,n,k-1,row+1,cols,count)   #回溯经典步骤
            cols[col]=0

    backtrack(board,n,k,row+1,cols,count)  #递归下一行，跳过改行

while True:
    n,k=map(int,input().split())
    if n==-1 and k==-1:
        break
    grid=[]
    for _ in range(n):
        grid.append(list(map(str,input())))
    cols=[0]*n
    count=[0]
    backtrack(grid,n,k,0,cols,count)
    print(count[0])