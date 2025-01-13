n=int(input())
a=bin(n)[2:]
m=len(a)
find=True
left,right=0,m-1
while left<=right:
    if a[left]!=a[right]:
        find=False
    left+=1
    right-=1
if find:
    print('Yes')
else:
    print('No')