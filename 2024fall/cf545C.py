n=int(input())
a=[]
for i in range(n):
    x,h=map(int,input().split())
    a.append([x,h])
f=a[0][0]
t=0
if n==1:
    t=1
elif  n==2:
    t=2
else:
    for i in range(1,n-1):
        x,h=a[i][0],a[i][1]
        if x-h>f:
            t+=1
            f=x
        elif x+h<a[i+1][0]:
            t+=1
            f=x+h
        else:
            f=x
    t+=2
print(t)