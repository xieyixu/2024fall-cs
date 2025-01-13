n=int(input())
a=[i+1 for i in range(n**2)]
M=[[0]*n for i in range(n)]
left=0;right=n-1;up=0;bottom=n-1
while up<=bottom and left<=right:
    for i in range(left,right+1):
        M[up][i]=a.pop(0)
    up+=1
    for i in range(up,bottom+1):
        M[i][right]=a.pop(0)
    right-=1
    if up<bottom:
        for i in range(right,left-1,-1):
            M[bottom][i]=a.pop(0)
        bottom-=1
    if left<right:
        for i in range(bottom,up-1,-1):
            M[i][left]=a.pop(0)
        left+=1
for s in M:
    for j in s:
        if j!=s[-1]:
            print(j,end=' ')
        else:
            print(j)