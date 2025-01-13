from collections import deque
n,m=map(int,input().split())
r=list(map(int,input().split()))
r.sort()
delta=[(r[i+1]-r[i]) for i in range(n-1)]
t=0
delta.sort()
delta=deque(delta)
for _ in range(m-1):    #从列表中移除最后一个元素是很慢的，这里要考虑使用双端队列或堆（heapq）
    delta.pop()
print(sum(delta))