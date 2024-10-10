def pairs(a,b):
    a=sorted(a)
    b=sorted(b)
    i=j=t=0
    while i<len(a) and j<len(b):
        if abs(a[i]-b[j])<=1:
            i+=1
            j+=1
            t+=1
        elif a[i]<b[j]:
            i+=1
        else:
            j+=1
    print(t)

n=int(input())
boys=list(map(int,input().split()))
m=int(input())
girls=list(map(int,input().split()))
pairs(boys,girls)