L,n,m=map(int,input().split())
stone=[0]
for _ in range(n):
    stone.append(int(input()))
stone.append(L)
def check(x):
    num=0
    now=0
    for i in range(1,n+2):
        if stone[i]-now<x:
            num+=1
        else:
            now=stone[i]
    if num>m:
        return True
    else:
        return False
left,right=0,L+1
answer=-1
while left<right:
    mid=(left+right)//2
    if check(mid):
        right=mid
    else:
        answer=mid
        left=mid+1
print(answer)