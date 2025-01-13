from collections import deque

directions=[(0,1),(0,-1),(1,0),(-1,0)]
def bfs(x1,y1,x2,y2,m,h,w):
    queue=deque([(x1,y1,-1,0)])
    visited=set()
    ans=[]
    while queue:
        x,y,dire,turns=queue.popleft()
        if (x,y)==(x2,y2):
            ans.append(turns)
            break

        for i,(dx,dy) in enumerate(directions):
            nx,ny=x+dx,y+dy
            if 0<=nx<h+2 and 0<=ny<w+2 and (nx,ny,i) not in visited:
                new_turn=turns if dire==i else turns+1
                if (nx,ny)==(x2,y2):
                    ans.append(new_turn)
                    continue
                if m[nx][ny]!='X':
                    visited.add((nx,ny,i))
                    queue.append((nx,ny,i,new_turn))
    if len(ans)==0:
        return -1
    else:
        return min(ans)

Board=1
while True:
    Pair=1
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    matrix=[]
    for _ in range(h):
        matrix.append(list(input()))
    new_matrix=[[' ']*(w+2) for _ in range(h+2)]
    for i in range(h):
        for j in range(w):
            new_matrix[i+1][j+1]=matrix[i][j]
    print(f'Board #{Board}:')
    while True:
        y1,x1,y2,x2=map(int,input().split())
        if x1==0 and x2==0 and y1==0 and y2==0:
            break
        segment=bfs(x1,y1,x2,y2,new_matrix,h,w)
        if segment==-1:
            print(f'Pair {Pair}: impossible.')
        else:
            print(f'Pair {Pair}: {segment} segments.')
        Pair+=1
    print()
    Board+=1