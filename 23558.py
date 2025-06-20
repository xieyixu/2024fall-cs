n, m, L = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
for i in range(n):
    adj[i].sort()

start = int(input())
visited = [False] * n
result = []

def dls(node, depth):
    if visited[node]:
        return
    visited[node] = True
    result.append(node)
    for neighbor in adj[node]:
        if not visited[neighbor]:
            if depth + 1 <= L:
                dls(neighbor, depth + 1)

dls(start, 0)
print(' '.join(map(str, result)))