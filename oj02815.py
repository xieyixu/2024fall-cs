m=int(input())
n=int(input())
a=[]
for _ in range(m):
    a.append(list(map(int,input().split())))
wall=[[list()]*(n) for _ in range(m)]
for i in range(m):
    for j in range(n):
        if a[i][j]==1:
            wall[i][j]=[(0,-1)]
        if a[i][j]==2:
            wall[i][j]=[(-1,0)]
        if a[i][j]==3:
            wall[i][j]=[(-1,0),(0,-1)]
        if a[i][j]==4:
            wall[i][j]=[(0,1)]
        if a[i][j]==5:
            wall[i][j]=[(0,1),(0,-1)]
        if a[i][j]==6:
            wall[i][j]=[(0,1),(-1,0)]
        if a[i][j]==7:
            wall[i][j]=[(0,1),(0,-1),(-1,0)]
        if a[i][j]==8:
            wall[i][j]=[(1,0)]
        if a[i][j]==9:
            wall[i][j]=[(1,0),(0,-1)]
        if a[i][j]==10:
            wall[i][j]=[(1,0),(-1,0)]
        if a[i][j]==11:
            wall[i][j]=[(1,0),(-1,0),(0,-1)]
        if a[i][j]==12:
            wall[i][j]=[(0,1),(1,0)]
        if a[i][j]==13:
            wall[i][j]=[(0,1),(1,0),(0,-1)]
        if a[i][j]==14:
            wall[i][j]=[(0,1),(1,0),(-1,0)]
        if a[i][j]==15:
            wall[i][j]=[(0,1),(1,0),(0,-1),(-1,0)]
directions=[(1,0),(0,1),(-1,0),(0,-1)]
visited=[[False]*n for _ in range(m)]
count=0
max_size=0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            stack = [(i, j)]
            visited[i][j]=True
            size=0
            while stack:
                x,y=stack.pop()
                size+=1
                visited[x][y]=True
                for dx,dy in directions:
                    if (dx,dy) not in wall[x][y]:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
                            stack.append((nx,ny))
                            visited[nx][ny]=True
            count+=1
            if size>max_size:
                max_size=size
print(count)
print(max_size)