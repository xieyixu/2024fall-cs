import heapq
directions=[(0,1),(0,-1),(1,0),(-1,0)]
def dfs(x1,y1,x2,y2,matrix,m,n):
    if matrix[x1][y1]=='#' or matrix[x2][y2]=='#':
        return 'NO'
    distance=[[float('inf')]*n for _ in range(m)]
    distance[x1][y1]=0
    pq=[(0,x1,y1)]
    while pq:
        cost,x,y=heapq.heappop(pq)
        if (x,y)==(x2,y2):
            return cost
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and matrix[nx][ny]!='#':
                new_cost=cost+abs(int(matrix[nx][ny])-int(matrix[x][y]))    #直接dfs过不了，会超时，要使用Dijkstra算法。这个算法有贪心的思想，核心是使用堆来极快提升查找速度
                if new_cost<distance[nx][ny]:
                    distance[nx][ny]=new_cost
                    heapq.heappush(pq,(new_cost,nx,ny))   #可以发现这个算法的代码看起来和dfs没有差太多，最主要是通过堆来优化。
    return 'NO'

m,n,p=map(int,input().split())
a=[input().split() for _ in range(m)]
case=[list(map(int,input().split())) for _ in range(p)]
answer=[]
for x1,y1,x2,y2 in case:
    result=dfs(x1,y1,x2,y2,a,m,n)
    answer.append(result)
for s in answer:
    print(s)