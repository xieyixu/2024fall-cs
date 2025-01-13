from collections  import deque
n,m=map(int,input().split())
a=list(map(int,input().split()))
dq=deque([(a[i],i) for i in range(n)])
while len(dq)>1:
    x,q=dq.popleft()
    x-=m
    if x>0:
        dq.append((x,q))
x,q=dq.pop()
print(q+1)