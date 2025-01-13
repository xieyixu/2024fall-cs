from collections import deque

n=int(input())
i=1
a=[]
while i*i<=n:
    a.append(i*i)
    i+=1
def bfs(n,a):
    queue=deque([(n,0)])
    while queue:
        for _ in range(len(queue)):
            x,count=queue.popleft()
            if x==0:
                return count
            else:
                for i in range(len(a)):
                    if x-a[i]>=0:
                        queue.append((x-a[i],count+1))
print(bfs(n,a))