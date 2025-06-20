# 23n2000012515(heol) 熊江凯
from collections import deque

sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
# blocks = set(tuple(map(int, input().split())) for _ in range(int(input())))
blocks = set()
for _ in range(int(input())):
    coordinates = tuple(map(int, input().split()))
    blocks.add(coordinates)

MAXD = 8
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [1, -1, -2, -2, -1, 1, 2, 2]

q = deque()
q.append((sx, sy, f'({sx},{sy})'))
inQueue = set()
inQueue.add((sx, sy))
ans = 0
cur_path = ''

while q:
    tmp = deque()
    while q:
        x, y, path = q.popleft()
        wx, wy = [-1, 0, 1, 0], [0, -1, 0, 1]
        if x == ex and y == ey:
            ans += 1
            if ans == 1:
                cur_path = path
        for i in range(MAXD):
            nx, ny = x + dx[i], y + dy[i]
            hx, hy = x + wx[i//2], y + wy[i//2]
            if (nx, ny) not in inQueue and (hx, hy) not in blocks:
                tmp.append((nx, ny, path + f'-({nx},{ny})'))

        inQueue.add((nx, ny))	# 避免重复入队列
    if ans:
        break
    q = tmp	# 等价于q.extend(tmp)

print(cur_path if ans == 1 else ans)