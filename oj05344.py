from collections import deque
n,k=map(int,input().split())
queue=deque(list(range(1,n+1)))
ans=[]
i=0
while queue:
    x=queue.popleft()
    i+=1
    if i==k:
        ans.append(x)
        i=0
    else:
        queue.append(x)
print(' '.join(map(str,ans[:n-1])))