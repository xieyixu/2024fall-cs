n,w=map(int,input().split())
a=[]
t=[]
for i in range(n):
    v,m=list(map(int,input().split()))
    if m!=0:
        average=v/m
        vma=[v,m,average]
        a.append(vma)
    else:
        average=0
        vma=[v,m,average]
        a.append(vma)
a.sort(key=lambda x:x[2],reverse=True)
m=0
v=0
for i in range(n):
    m=m+a[i][1]
    v=v+a[i][1]*a[i][2]
    if m>w:
        v=v-a[i][2]*(m-w)
        m=m-a[i][1]
        break
print(round(v,1))