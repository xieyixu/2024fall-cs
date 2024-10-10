beautiful_matrix=[]
for i in range(5):
    bm=list(map(int,input().split()))
    beautiful_matrix.append(bm)

for i in range(5):
    for j in range(5):
        if beautiful_matrix[i][j]==1:
            print(abs(i-2)+abs(j-2))