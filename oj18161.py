A,B,C=[],[],[]
r_A,c_A=map(int,input().split())
for _ in range(r_A):
    A.append(list(map(int,input().split())))
r_B,c_B=map(int,input().split())
for _ in range(r_B):
    B.append(list(map(int,input().split())))
r_C,c_C=map(int,input().split())
for _ in range(r_C):
    C.append(list(map(int,input().split())))
if c_A!=r_B or r_A!=r_C or c_B!=c_C:
    print('Error!')
else:
    answer=[[0]*c_B for _ in range(r_A)]
    for i in range(r_A):
        for j in range(c_B):
            for k in range(c_A):
                answer[i][j]+=A[i][k]*B[k][j]
    for i in range(r_A):
        for j in range(c_C):
            answer[i][j]+=C[i][j]
    for i in range(r_A):
        print(' '.join(map(str,answer[i])))