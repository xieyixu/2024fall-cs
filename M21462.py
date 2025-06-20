n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
l=[]
top,bottom=0,n-1
left,right=0,n-1
while top<=bottom and left<=right:
    for i in range(top,bottom+1):
        l.append(matrix[i][left])
    left+=1
    for i in range(left,right+1):
        l.append(matrix[bottom][i])
    bottom-=1
    for i in range(bottom,top-1,-1):
        l.append(matrix[i][right])
    right-=1
    for i in range(right,left-1,-1):
        l.append(matrix[top][i])
    top+=1
answer=[]
for num in l:
    if num:
        answer.append(chr(num))
print(''.join(answer))