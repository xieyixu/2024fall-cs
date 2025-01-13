from collections import deque

directions=[(0,1),(0,-1),(1,0),(-1,0)]
def bfs(start,end,R,C,K,matrix):
    queue=deque([(start[0],start[1],0)])
    visited={(start[0],start[1],0)}
    while queue:
        x,y,step=queue.popleft()
        if (x,y)==end:
            return step
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<R and 0<=ny<C and ((step+1)%K==0 or ((step+1)%K!=0 and matrix[nx][ny]!='#')) and (nx,ny,(step+1)%K) not in visited:
                queue.append((nx,ny,step+1))
                visited.add((nx,ny,(step+1)%K))
    return -1

T=int(input())
for _ in range(T):
    R, C, K = map(int, input().split())
    a = [input() for _ in range(R)]
    x1, y1, x2, y2 = 0, 0, 0, 0
    for i in range(R):
        for j in range(C):
            if a[i][j] == 'S':
                x1, y1 = i, j
            if a[i][j] == 'E':
                x2, y2 = i, j
    start = (x1, y1)
    end=(x2,y2)
    result=bfs(start,end,R,C,K,a)
    if result>=0:
        print(result)
    else:
        print('Oop!')