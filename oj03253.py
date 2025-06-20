from collections import deque
while True:
    n,p,m=map(int,input().split())
    if n==0 and p==0 and m==0:
        break
    l=deque(list(range(p,n+1))+list(range(1,p)))
    ans=deque()
    while l:
        for i in range(m):
            ans.append(l.popleft())
            if i<m-1:
                l.append(ans.pop())
    print(','.join(map(str,list(ans))))