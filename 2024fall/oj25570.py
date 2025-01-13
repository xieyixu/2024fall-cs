n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
a=0
if n%2==0:
    a=n/2
elif n%2==1:
    a=(n+1)/2
i=0
max_sum=float('-inf')
while i<a:
    sum=0
    for j in range(i,n-i):
        sum+=matrix[i][j]
        matrix[i][j] = 0
    for j in range(i,n-i):
        sum+=matrix[n-i-1][j]
        matrix[n-1-i][j]=0
    for j in range(i,n-i):
        sum+=matrix[j][i]
        matrix[j][i] = 0
    for j in range(i,n-i):
        sum+=matrix[j][n-1-i]
        matrix[n-i-1][j]=0
    max_sum=max(sum,max_sum)
    i+=1
print(max_sum)