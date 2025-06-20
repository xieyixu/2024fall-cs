n,m=map(int,input().split())
matrix=[]
for _ in range(n):
    matrix.append(list(map(int,input().split())))
answer=[[0]*m for _ in range(n)]
directions=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
for x in range(n):
    for y in range(m):
        count=0
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                count+=matrix[nx][ny]
        if matrix[x][y]==0:
            if count==3:
                answer[x][y]=1
            else:
                answer[x][y]=0
        if matrix[x][y]==1:
            if count<2:
                answer[x][y]=0
            elif count>3:
                answer[x][y]=0
            else:
                answer[x][y]=1
for i in range(n):
    print(' '.join(map(str,answer[i])))