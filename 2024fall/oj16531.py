from collections import Counter
M,N=map(int,input().split())
grid=[]
for _ in range(M):
    grid.append(list(map(int,input().split())))
a=[]
b=[]
for _ in range(M*N):
    data=list(map(int,input().split()))
    a.append(data)
    b.append(sum(data))
directions=[(0,1),(0,-1),(1,0),(-1,0)]
count={(-1,-1)}
for x in range(M):
    for y in range(N):
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<M and 0<=ny<N:
                if a[grid[x][y]]==a[grid[nx][ny]]:
                    count.add((x,y))
                    count.add((nx,ny))
result_1=len(count)-1
b_count=Counter(b)
sort_b_count=list(sorted(b_count.items(),reverse=True))
result_2=0
for s in sort_b_count:
    if result_2+s[1]<=M*N*0.4:
        result_2+=s[1]
    else:
        break
print(result_1,result_2)