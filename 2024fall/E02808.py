L,M=map(int,input().split())
a=[1]*(L+1)
for i in range(M):
    x1,x2=map(int,input().split())
    for j in range(x1,x2+1):
        a[j]=0
print(sum(a))