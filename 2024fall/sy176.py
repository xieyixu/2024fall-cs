m,n=map(int,input().split())
M=list(map(int,input().split()))
N=list(map(int,input().split()))
K=M+N
K.sort()
J=[str(k) for k in K]
print(" ".join(J))