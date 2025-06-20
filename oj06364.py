N,K=map(int,input().split())
A=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append((i+1,a,b))
B=[]
A.sort(key=lambda x:-x[1])
for i in range(K):
    B.append(A[i])
B.sort(key=lambda x:-x[2])
print(B[0][0])