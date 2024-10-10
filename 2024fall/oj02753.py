n=int(input())
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
for i in range(n):
    p=1
    q=0
    if a[i]==1 or a[i]==2:
        print(1)
    else:
        for t in range(a[i]):
            p,q=q,p+q
        print(q)