n,m1,m2=map(int,input().split())
X=[];Y=[]
Z=[[0]*n for _ in range(n)]
for i in range(m1):
    row,col,x=map(int,input().split())
    X.append([row,col,x])
X.sort()
for i in range(m2):
    row,col,y=map(int,input().split())
    Y.append([row,col,y])
Y.sort()
for i in range(m1):
    for j in range(m2):
        if X[i][1]==Y[j][0]:
            Z[X[i][0]][Y[j][1]]+=X[i][2]*Y[j][2]
for i in range(n):
    for j in range(n):
        if Z[i][j]!=0:
            print(f"{i} {j} {Z[i][j]}")