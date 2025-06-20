from collections import deque
start=tuple(map(int,input().split()))
end=tuple(map(int,input().split()))
m=int(input())
l=[]
for _ in range(m):
    x,y=map(int,input().split())
    l.append((x,y))
directions=[(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]
prev={start:[]}
queue=deque([(start[0],start[1],f'({start[0]},{start[1]})')])
visited={start}
count=0
ans=''
while queue:
    tmp=deque()
    while queue:
        x,y,path=queue.popleft()
        if (x,y)==end:
            count+=1
            if count==1:
                ans=path
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if (nx,ny) not in visited:
                if dx==2:
                    if (x+1,y) not in l:
                        tmp.append((nx,ny,path+f'-({nx},{ny})'))
                elif dx==-2:
                    if (x-1,y) not in l:
                        tmp.append((nx,ny,path+f'-({nx},{ny})'))
                elif dy==2:
                    if (x,y+1) not in l:
                        tmp.append((nx, ny,path+f'-({nx},{ny})'))
                elif dy==-2:
                    if (x,y-1) not in l:
                        tmp.append((nx, ny,path+f'-({nx},{ny})'))
    for node in tmp:
        visited.add((node[0],node[1]))
    if count:
        break
    queue=tmp

print(ans if count==1 else count)