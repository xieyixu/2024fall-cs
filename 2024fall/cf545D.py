n=int(input())
a=list(map(int,input().split()))
a.sort()
s=0
t=0
i=0
while i<n:
    if a[i]>=s:
        s+=a[i]
        t+=1
    i+=1
print(t)