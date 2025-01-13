import bisect
m,n,x=map(int,input().split())
matrix=[]
for _ in range(m):
    matrix.append(list(map(int,input().split())))
a=[matrix[i][0] for i in range(m)]
b=bisect.bisect(a,x)
set=set(matrix[b-1])
if x in set:
    print('True')
else:
    print('False')  #这个方法并不好，最快的是展平一个矩阵然后直接二分查找。