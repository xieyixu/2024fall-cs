n,a,b=map(int,input().split())
v=list(map(int,input().split()))
Alice,Bob=0,n-1
count=0
A,B=a,b
while Alice<=Bob:
    if Alice==Bob:
        if A>=B:
            if A<v[Alice]:
                count+=1
        else:
            if B<v[Bob]:
                count+=1
    else:
        if A>=v[Alice]:
            A-=v[Alice]
        else:
            A=a-v[Alice]
            count+=1
        if B>=v[Bob]:
            B-=v[Bob]
        else:
            B=b-v[Bob]
            count+=1
    Alice+=1
    Bob-=1
print(count)