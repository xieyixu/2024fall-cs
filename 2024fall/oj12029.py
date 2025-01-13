import sys
sys.setrecursionlimit(300000)
from collections import deque
direction=[(0,1),(0,-1),(1,0),(-1,0)]
def bfs(X,Y,M,N,matrix,I,J):
    query=deque([(X,Y)])
    visited=[[False]*N for _ in range(M)]
    visited[X][Y]=True
    while query:
        x,y=query.popleft()
        if x==I and y==J:
            return True
        for dx,dy in direction:
            nx,ny=x+dx,y+dy
            if 0<=nx<M and 0<=ny<N and matrix[nx][ny]<matrix[X][Y] and not visited[nx][ny]:
                query.append((nx,ny))
                visited[nx][ny]=True
    return False

input_data=sys.stdin.read().split()
index=0
K=int(input_data[index])
index+=1
answer=[]
for _ in range(K):
    M,N=map(int,input_data[index:index+2])
    index+=2
    matrix=[]
    for _ in range(M):
        matrix.append(list(map(int,input_data[index:index+N])))
        index+=N
    I,J=map(int,input_data[index:index+2])
    I,J=I-1,J-1
    index+=2
    P=int(input_data[index])
    index+=1
    W=[]
    for _ in range(P):
        X,Y=map(int,input_data[index:index+2])
        W.append((X-1,Y-1))
        index+=2
    bool=False
    for X,Y in W:
        if bfs(X,Y,M,N,matrix,I,J):
            bool=True
            break
    if bool:
        answer.append('Yes')
    else:
        answer.append('No')
for s in answer:
    print(s)