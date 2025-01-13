import math
def get_next_permutation(a):
    n=len(a)
    i=n-2
    while i>=0 and a[i]>=a[i+1]:
        i-=1
    if i==-1:
        return sorted(a)
    j=n-1
    while j>=0 and a[i]>a[j]:
        j-=1
    a[i],a[j]=a[j],a[i]
    a[i+1:]=reversed(a[i+1:])
    return a

m=int(input())
answers=[]
for _ in range(m):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    i=0
    k=k%math.factorial(n)
    while i<k:
        a=get_next_permutation(a)
        i+=1
    answers.append(a)
for a in answers:
    for s in a:
        if s!=a[-1]:
            print(s,end=' ')
        else:
            print(s)