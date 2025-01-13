n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
start=[]
end=()
for i in range(n):
    for j in range(n):
        if a[i][j]==9:
            end=(i,j)
        if a[i][j]==5:
            start.append((i,j))
visited_1=[[False]*n for _ in range(n)]
visited_2=[[False]*n for _ in range(n)]
visited_1[start[0][0]][start[0][1]]=True
visited_2[start[1][0]][start[1][1]]=True
def dfs(start,end,n,grid):
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    stack_1=[start[0]]
    stack_2=[start[1]]
    while stack_1 and stack_2:
        x1,y1=stack_1.pop()
        x2,y2=stack_2.pop()
        if (x1,y1)==end or (x2,y2)==end:
            return True
        for dx,dy in directions:
            nx1,ny1,nx2,ny2=x1+dx,y1+dy,x2+dx,y2+dy
            if 0<=nx1<n and 0<=nx2<n and 0<=ny1<n and 0<=ny2<n:
                if not visited_1[nx1][ny1] and not visited_2[nx2][ny2]:
                    if grid[nx1][ny1]!=1 and grid[nx2][ny2]!=1:
                        stack_1.append((nx1,ny1))
                        stack_2.append((nx2,ny2))
                        visited_1[nx1][ny1]=True
                        visited_2[nx2][ny2]=True
    return False
if dfs(start,end,n,a):
    print('yes')
else:
    print('no')