from collections import deque
n,k=map(int,input().split())
a=list(map(int,input().split()))
dq=deque()
answer=[]
for i in range(n):
    if dq and dq[0]<i-k+1:
        dq.popleft()
    while dq and a[dq[-1]]<a[i]:
        dq.pop()
    dq.append(i)
    if i>=k-1:
        answer.append(a[dq[0]])
for s in answer:
    print(s,end=' ')