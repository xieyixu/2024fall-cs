m,n=map(int,input().split())
M=[]
a=[]
for _ in range(m):
    M.append(list(map(int,input().split())))
left,right,up,down=0,n-1,0,m-1
while left<=right and up<=down:
    for i in range(left,right+1):
        a.append(M[up][i])
    up+=1
    for i in range(up,down+1):
        a.append(M[i][right])
    right-=1
    if up<=down:
        for i in range(right,left-1,-1):
            a.append(M[down][i])
        down-=1
    if left<=right:
        for i in range(down,up-1,-1):
            a.append(M[i][left])
        left+=1
print(a)