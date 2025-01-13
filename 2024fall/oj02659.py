from collections import Counter

A,B,K=map(int,input().split())
M=[list(map(int,input().split()))for _ in range(K)]
N = [[0] * B for _ in range(A)]

def check(A,B,R,S,P,T):
    for i in range(max(R-1-int((P-1)/2),0),min(R+int((P-1)/2),A)):
        for j in range(max(S-1-int((P-1)/2),0),min(S+int((P-1)/2),B)):
            if T==1:
                N[i][j]+=1
            if T==0:
                N[i][j]-=100
    return N

for i in range(K):
    R,S,P,T=M[i][0],M[i][1],M[i][2],M[i][3]
    check(A,B,R,S,P,T)

N1=[element for row in N for element in row]
counter=Counter(N1)
max_N1=max(N1)
print(counter[max_N1])