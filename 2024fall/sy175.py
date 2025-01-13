n,k=map(int,input().split())
A=list(map(int,input().split()))
B=set(A)
t=0
for i in range(len(A)):
    if k-A[i] in B:
        t+=1
print(int(t/2))