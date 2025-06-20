from collections import deque
T=int(input())
directions=[(0,1),(1,0),(-1,0),(0,-1)]
for _ in range(T):
    R,C=map(int,input().split())
    board=[list(input()) for _ in range(R)]
    start=(0,0)
    end=(0,0)
    for i in range(R):
        for j in range(C):
            if board[i][j]=='S':
                start=(i,j)
            if board[i][j]=='E':
                end=(i,j)
    queue=deque([(start[0],start[1],0)])
    visited=set()
    visited.add(start)
    ans=0
    while queue:
        x,y,t=queue.popleft()
        if (x,y)==end:
            ans=t
            break
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<R and 0<=ny<C and (nx,ny) not in visited:
                if board[nx][ny]!='#':
                    visited.add((nx,ny))
                    queue.append((nx,ny,t+1))
    if ans!=0:
        print(ans)
    else:
        print('oop!')
