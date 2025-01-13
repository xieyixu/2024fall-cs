m,n,p,q=map(int,input().split())
M=[]
P=[]
for i in range(m):
    M.append(list(map(int,input().split())))
for i in range(p):
    P.append(list(map(int,input().split())))
S=[]
for i in range(m-p+1):
    s=[]
    for t in range(n-q+1):
        sum=0
        for k in range(p):
            for j in range(q):
                sum+=P[k][j]*M[i+k][t+j]
        s.append(sum)
    S.append(s)
for s in S:
    print(" ".join(map(str,s)))