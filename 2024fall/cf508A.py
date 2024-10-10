n,m,k=map(int,input().split())
a=[[False]*(m+2) for i in range(n+2)]
def check(i,j):
    if a[i-1][j] and a[i][j-1] and a[i-1][j-1]:
        return True
    elif a[i+1][j] and a[i][j+1] and a[i+1][j+1]:
        return True
    elif a[i-1][j] and a[i][j+1] and a[i-1][j+1]:
        return True
    elif a[i+1][j] and a[i][j-1] and a[i+1][j-1]:
        return True
    return False
found=False
T=[]
for i in range(1,k+1):
    x,y=map(int,input().split())
    a[x][y]=True
    if check(x,y):
        found=True
        T.append(i)
if not found:
    print(0)
else:
    print(min(T))