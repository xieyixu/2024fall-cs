n,q=map(int,input().split())
a=[]
for i in range(q):
    x,y=map(int,input().split())
    t=[x,y]
    a.append(t)
found=True
for i in range(q):
    for j in range(i,q):
        if a[i][0]==a[j][1] and a[i][1]==a[j][0]:
            print('Yes')
            found=False
            break
if found:
    print('No')