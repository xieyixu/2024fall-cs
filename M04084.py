import heapq
v, a = map(int, input().split())
adj = [[] for _ in range(v + 1)]
in_degree = [0] * (v + 1)
for _ in range(a):
    u, w = map(int, input().split())
    adj[u].append(w)
    in_degree[w] += 1
heap = []
for i in range(1, v + 1):
    if in_degree[i] == 0:
        heapq.heappush(heap, i)
result = []
while heap:
    u = heapq.heappop(heap)
    result.append(u)
    for neighbor in adj[u]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            heapq.heappush(heap, neighbor)
print(' '.join(['v{}'.format(x) for x in result]))