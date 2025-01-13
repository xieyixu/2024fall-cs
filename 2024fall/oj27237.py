from collections import deque
import math
def bfs(n,m):
    if n==m:
        return 0,''
    queue=deque([(n,0,'')])
    visited=set()
    visited.add(n)
    while queue:
        x,count,path=queue.popleft()
        if x==m:
            return count,path
        if count<=25:
            x1,count1,path1=3*x,count+1,path+'H'
            x2,count2,path2=math.floor(x/2),count+1,path+'O'
            if x1 not in visited:
                visited.add(x1)
                queue.append((x1,count1,path1))
            if x2 not in visited:
                visited.add(x2)
                queue.append((x2,count2,path2))
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    k,p=bfs(n,m)
    print(k)
    print(p)