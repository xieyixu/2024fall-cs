from collections import deque
directions=[(0,1),(0,-1),(1,0),(-1,0)]
def bfs(a,n,queue):
    count=0
    while queue:
        for _ in range(len(queue)):
            x,y=queue.popleft()
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n:
                    if a[nx][ny]==0:
                        a[nx][ny]=2
                        queue.append((nx,ny))
                    elif a[nx][ny]==1:
                        return count
        count+=1
    return count
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input())))
x1,y1=0,0
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            x1,y1=i,j
            break
stack_1=[(x1,y1)]
a[x1][y1]=2
visited_1=[[False]*(n) for _ in range(n)]
visited_1[x1][y1]=True
queue=deque([(x1,y1)])
while stack_1:
    x,y=stack_1.pop()
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and not visited_1[nx][ny] and a[nx][ny]==1: #找出一个岛
            visited_1[nx][ny]=True
            a[nx][ny]=2
            stack_1.append((nx,ny))
            queue.append((nx,ny))
print(bfs(a,n,queue))