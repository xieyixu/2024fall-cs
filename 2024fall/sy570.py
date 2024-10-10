n,q=map(int,input().split())
T=[]
for i in range(q):
    x,y=map(int,input().split())
    t=[x,y]
    T.append(t)
found=False
for i in range(q):
    for j in range(i,q):
        for k in range(i,q):
            if T[i][0]==T[j][1] and T[j][0]==T[k][1] and T[k][0]==T[i][1]:
                print('Yes')
                found=True
                break
if not found:
    print('No')