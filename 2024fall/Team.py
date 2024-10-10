a=int(input())
i=0
m=0
while i<a:
    p,v,n=map(int,input().split())
    i+=1
    if p+v+n>1:
        m=m+1

print(m)