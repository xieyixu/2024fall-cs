a1,b1=map(int,input().split())
A=[]
for _ in range(a1):
    number=list(map(int,input().split()))
    A.append(number)
a2,b2=map(int,input().split())
B=[]
for _ in range(a2):
    number=list(map(int,input().split()))
    B.append(number)
a3,b3=map(int,input().split())
C=[]
for _ in range(a3):
    number=list(map(int,input().split()))
    C.append(number)
if a2!=b1 or a3!=a1 or b3!=b2:
    print("Error!")
else:
    AB=[[sum(A[i][k]*B[k][j]for k in range(a2))for j in range(b2)]for i in range(a1)]
    ABC=[[AB[i][j]+C[i][j]for j in range(b2)]for i in range(a1)]
    for i in range(a1):
        for j in range(b2):
            if j!=b2-1:
                print(ABC[i][j],end=' ')
            else:
                print(ABC[i][j],end='\n')