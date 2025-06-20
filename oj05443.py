import heapq
def dijkstra(adj,start,end,num_nodes):
    dist=[float('inf')]*num_nodes
    prev=[None]*num_nodes
    dist[start]=0
    heap=[]
    heapq.heappush(heap,(0,start))
    while heap:
        current_dist,u=heapq.heappop(heap)
        if u==end:
            break
        if current_dist>dist[u]:
            continue
        for v in adj[u]:
            weight=adj[u][v]
            if dist[v]>dist[u]+weight:
                dist[v]=dist[u]+weight
                prev[v]=u
                heapq.heappush(heap,(dist[v],v))
    path=[]
    current=end
    if prev[current] is None and start!=end:
        return None
    while current is not None:
        path.append(current)
        current=prev[current]
    path.reverse()
    if not path or path[0]!=start:
        return None
    return path


def main():
    P=int(input())
    name_to_index={}
    places=[]
    for i in range(P):
        name=input().strip()
        places.append(name)
        name_to_index[name]=i
    adj=[{} for _ in range(P)]
    Q=int(input())
    for _ in range(Q):
        p1,p2,l=input().split()
        distance=int(l)
        u=name_to_index[p1]
        v=name_to_index[p2]
        adj[u][v]=distance
        adj[v][u]=distance
    R=int(input())
    for _ in range(R):
        start,end=input().split()
        if start==end:
            print(start)
            continue
        u=name_to_index.get(start)
        v=name_to_index.get(end)
        path=dijkstra(adj, u, v, P)
        res=places[path[0]]
        for i in range(1,len(path)):
            prev_node=path[i-1]
            curr_node=path[i]
            res+=f"->({adj[prev_node][curr_node]})->{places[curr_node]}"
        print(res)

if __name__=="__main__":
    main()