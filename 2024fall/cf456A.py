n=int(input())
t=[]
for _ in range(n):
    p,q=map(int,input().split())
    t.append((p,q))
t1=sorted(t,key=lambda x:(x[0]))
t2=sorted(t,key=lambda x:(x[1]))
if t1==t2:
    print("Poor Alex")
else:
    print("Happy Alex")