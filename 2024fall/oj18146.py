n,k=map(int,input().split())
a=list(map(int,input().split()))
c=[0]*4
for i in range(k):
    c[a[i]%4]+=1
add=c[1]+c[3]
t=c[2]-2*n-c[1]
if t>0:
    add+=t//3*2
    if t%3==1:
        add+=2
    if t%3==2:
        add+=4
print('YES' if sum(a)+add<=n*8 else 'NO')