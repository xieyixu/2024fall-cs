directions=[(0,1),(0,-1),(1,0),(-1,0)]
def dfs(i,j,board):
    board[i][j]='Y'
    stack=[(i,j)]
    while stack:
        x,y=stack.pop()
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and board[nx][ny]=='O':
                stack.append((nx,ny))
                board[nx][ny]='Y'
m,n=int(input())
board=[input().split() for _ in range(m)]
for i in range(n):
    if board[0][i]=='O':
        dfs(0,i,board)
    if board[m-1][i]=='O':
        dfs(m-1,i,board)
for i in range(m):
    if board[i][0]=='O':
        dfs(i,0,board)
    if board[i][n-1]=='O':
        dfs(i,n-1,board)
for i in range(m):
    for j in range(n):
        if board[i][j]!='Y':
            board[i][j]='X'
        else:
            board[i][j]='O'