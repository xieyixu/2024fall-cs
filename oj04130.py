import heapq
while True:
    N,M=map(int,input().split())
    if N==0 and M==0:
        break
    board=[]
    for _ in range(N):
        board.append(list(map(str,input())))
    start=(0,0,0,-1,0,[])
    for i in range(N):
        for j in range(N):
            if board[i][j]=='K':
                start=(0,i,j,0,[])
                break
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    queue=[start]
    visited=set()
    visited.add((start[1],start[2],start[3],start[4]))
    while queue:
        t,x,y,key,snake=heapq.heappop(queue)
        if board[x][y]=='T' and  key==M:
            print(t)
            break
        for i in range(4):
            nt,nx,ny=t+1,x+directions[i][0],y+directions[i][1]
            if 0<=nx<N and 0<=ny<N and board[nx][ny]!='#' and (nx,ny,key) not in visited:
                if board[nx][ny]=='S':
                    if (nx,ny) not in snake:
                        snake.append((nx,ny))
                        heapq.heappush(queue,(nt+1,nx,ny,key,snake))
                    else:
                        heapq.heappush(queue,(nt,nx,ny,key,snake))
                elif board[nx][ny]==str(key+1):
                    heapq.heappush(queue,(nt,nx,ny,key+1,snake))
                else:
                    heapq.heappush(queue,(nt,nx,ny,key,snake))
                visited.add((nx,ny,key))
    else:
        print('impossible')