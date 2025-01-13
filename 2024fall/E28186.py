from math import ceil
n,m=map(int,input().split())
a=list(map(int,input().split()))
a=[ceil(a[i]/m) for i in range(n)]
max=a[0]
t=1
for i in range(n):
    if a[i]>=max:
        max=a[i]
        t=i+1
print(t)