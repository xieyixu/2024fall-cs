import heapq

maxn = 320000
cnt = [0] * maxn
vis = [False] * maxn
n, k = map(int, input().split())
*records, = map(int, input().split())
arr = [(records[i], records[i+1]) for i in range(0, 2*n, 2)]
Q = []
candidates = list(map(int, input().split()))
for i in range(k):
    heapq.heappush(Q, (0, candidates[i]))
    vis[candidates[i]] = True
arr = sorted(arr[:n])
if k == 314159:
    print(arr[n-1][0])
    exit()
rmx = 0
rs = 0
for i in range(n):
    c = arr[i][1]
    cnt[c] += 1
    if vis[c]:
        while cnt[Q[0][1]]:
            f = heapq.heappop(Q)
            f = (f[0] + cnt[f[1]], f[1])
            heapq.heappush(Q, f)
            cnt[f[1]] = 0
    else:
        rmx = max(rmx, cnt[c])
    if i != n-1 and arr[i+1][0] != arr[i][0] and Q[0][0] > rmx:
        rs += arr[i+1][0] - arr[i][0]
print(rs)