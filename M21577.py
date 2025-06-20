m,n=map(int,input().split())
matrix=[]
for _ in range(m):
    matrix.append(list(map(int,input().split())))
height=[0]*n
max_area=0
for i in range(m):
    for j in range(n):
        if matrix[i][j]==0:
            height[j]+=1
        else:
            height[j]=0
    for j in range(n):
        if height[j]==0:
            continue
        left_bound=-1
        k=j-1
        while k>=0:
            if height[k]<height[j]:
                left_bound=k
                break
            k-=1
        right_bound=n
        k=j+1
        while k<n:
            if height[k]<height[j]:
                right_bound=k
                break
            k+=1
        width=right_bound-left_bound-1
        area=height[j]*width
        max_area=max(area,max_area)
print(max_area)