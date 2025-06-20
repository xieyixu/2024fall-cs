n=int(input())
N=2*n-1
matrix=[[0]*N for _ in range(N)]
matrix[0][N//2]=1
x,y=0,N//2
for i in range(1,N*N):
    new_x,new_y=x-1,y+1
    if 0<=new_x<N and 0<=new_y<N and matrix[new_x][new_y]==0:
        matrix[new_x][new_y]=i+1
    else:
        if new_x<0 and new_y>=N:
            new_x,new_y=N-1,0
        elif new_x<0:
            new_x,new_y=N-1,new_y
        elif new_y>=N:
            new_x,new_y=new_x,0
        if 0<=new_x<N and 0<=new_y<N and matrix[new_x][new_y]!=0:
            new_x,new_y=x+1,y
        matrix[new_x][new_y] = i + 1
    x,y=new_x,new_y
for s in matrix:
    print(' '.join(map(str,s)))