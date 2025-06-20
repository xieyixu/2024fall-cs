N,M=map(int,input().split())
cost=[]
for _ in range(N):
    money=int(input())
    cost.append(money)
x,y=max(cost),sum(cost)
count=1
def check(M,max_cost):
    current=0
    b=1
    for c in cost:
        if current+c>max_cost:
            b+=1
            current=c
            if b>M:
                return False
        else:
            current+=c
    return True
while x<y:
    mid=(x+y)//2
    if check(M,mid):
        y=mid
    else:
        x=mid+1
print(y)