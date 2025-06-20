n,m=map(int,input().split())
graph={i:[] for i in range(n)}
matrix=[[0]*n for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    matrix[a][b]=-1
    matrix[b][a]=-1
for i in range(n):
    matrix[i][i]=len(graph[i])
for s in matrix:
    print(' '.join(list(map(str,s))))