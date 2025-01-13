t=int(input())
S=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    s1=0
    s2=0
    s1+=sum(a)+n*min(b)
    s2+=sum(b)+n*min(a)
    S.append(min(s1,s2))
for s in S:
    print(s)