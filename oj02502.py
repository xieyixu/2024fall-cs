import sys
from collections import defaultdict
import heapq
import math

lines=[line.strip() for line in sys.stdin]
s_x,s_y,e_x,e_y=map(int,lines[0].split())
subway_lines=[]
for line in lines[1:]:
    if not lines:
        continue
    parts=list(map(int,line.split()))
    stations=[]
    i=0
    while i<len(parts):
        x=parts[i]
        y=parts[i+1]
        if x==-1 and y==-1:
            break
        stations.append((x,y))
        i+=2
    subway_lines.append(stations)
coords=set()
coords.add((s_x,s_y))
coords.add((e_x,e_y))
for line in subway_lines:
    for (x,y) in line:
        coords.add((x,y))
coords_list=list(coords)
coord_to_id={coord: idx for idx,coord in enumerate(coords_list)}
home_id=coord_to_id[(s_x,s_y)]
school_id=coord_to_id[(e_x,e_y)]

adj=defaultdict(list)
for line in subway_lines:
    for i in range(len(line)-1):
        x1,y1=line[i]
        x2,y2=line[i+1]
        u=coord_to_id[(x1,y1)]
        v=coord_to_id[(x2,y2)]
        distance=math.hypot(x2-x1,y2-y1)
        subway_time=distance*0.0015
        adj[u].append((v, subway_time))
        adj[v].append((u, subway_time))
n=len(coords_list)
for i in range(n):
    for j in range(i+1,n):
        x1,y1=coords_list[i]
        x2,y2=coords_list[j]
        distance=math.hypot(x2-x1,y2-y1)
        walk_time=distance*0.006
        adj[i].append((j,walk_time))
        adj[j].append((i,walk_time))
INF=float('inf')
dist=[INF]*n
dist[home_id]=0
heap=[(0,home_id)]
visited=set()

while heap:
    current_time,u=heapq.heappop(heap)
    if u in visited:
        continue
    visited.add(u)
    if u==school_id:
        break
    for v,time in adj[u]:
        if current_time+time<dist[v]:
            dist[v]=current_time+time
            heapq.heappush(heap,(dist[v],v))
result=dist[school_id]
rounded=int(result+0.5)
print(rounded)