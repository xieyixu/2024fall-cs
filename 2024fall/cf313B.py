s=input()
m=int(input())
T=[]
p=[0]*len(s)
t=0
for i in range(1,len(p)):
    if s[i]==s[i-1]:
        p[i]=p[i-1]+1
    else:
        p[i]=p[i-1]
for i in range(m):
    a,b=map(int,input().split())
    t=p[b-1]-p[a-1]
    T.append(t)
for t in T:
    print(t)