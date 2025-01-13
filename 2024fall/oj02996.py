def get_next_permutation(a):
    n=len(a)
    i=n-2
    while i>=0 and a[i]>a[i+1]:
        i-=1
        if i==-1:
            return sorted(a)
    j=n-1
    while j>=0 and a[i]>a[j]:
        j-=1
    a[i],a[j]=a[j],a[i]
    a[i+1:]=reversed(a[i+1:])
    return a

n=int(input())
m=int(input())
a=list(map(int,input().split()))
for i in range(m):
    a=get_next_permutation(a)
for s in a:
    if s!=a[-1]:
        print(s,end=' ')
    else:
        print(s)