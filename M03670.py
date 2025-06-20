matrix=[]
for _ in range(5):
    matrix.append(list(map(int,input().split())))
row_max=[]
for i in range(5):
    max_num=max(matrix[i])
    for j in range(5):
        if matrix[i][j]==max_num:
            row_max.append((i,j))
col_min=[]
for j in range(5):
    min_num=min(matrix[i][j] for i in range(5))
    for i in range(5):
        if matrix[i][j]==min_num:
            col_min.append((i,j))
x,y=0,0
found=False
for i in range(5):
    if col_min[i] in row_max:
        x,y=col_min[i]
        found=True
        break
if found:
    print(x+1,y+1,matrix[x][y])
else:
    print('not found')