k=int(input())
directions=[(0,1),(1,0),(0,-1),(-1,0)]
for _ in range(k):
    n=int(input())
    matrix=[]
    for _ in range(n):
        matrix.append(list(input()))
    visited_r=set()
    count_r=0
    for i in range(n):
        for j in range(n):
            if matrix[i][j]=='r':
                if (i,j) not in visited_r:
                    queue=[(i,j)]
                    visited_r.add((i,j))
                    while queue:
                        x,y=queue.pop()
                        for dx,dy in directions:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<n and 0<=ny<n and matrix[nx][ny]=='r' and (nx,ny) not in visited_r:
                                visited_r.add((nx,ny))
                                queue.append((nx,ny))
                    count_r+=1
    visited_b=set()
    count_b = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'b':
                if (i, j) not in visited_b:
                    queue = [(i, j)]
                    visited_b.add((i, j))
                    while queue:
                        x, y = queue.pop()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 'b' and (nx, ny) not in visited_b:
                                visited_b.add((nx, ny))
                                queue.append((nx, ny))
                    count_b += 1
    print(count_r,count_b)