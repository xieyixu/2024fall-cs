def function(n):
    a=[]
    for i in range(n):
        a.append(1)
    for i in range(1,n+1):
        for j in range(n):
            if (j+1)%i==0:
                a[j]=a[j]*(-1)
    t=0
    for _ in range(n):
        if a[_]==-1:
            t+=1
    print(t)

n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))

for _ in range(n):
    function(a[_])