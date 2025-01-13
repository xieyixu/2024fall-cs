n,M=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for i in range(1,n,2):
    b.append(a[i]-a[i-1])
if n%2==1:
    b.append(M-a[n-1])
