def count(a,start):
    if a==1:
        return 1
    ans=0
    for i in range(start,int(a**0.5)+1):
        if a%i==0:
            ans+=count(a//i,i)
    if a>=start:
        ans+=1
    return ans
n=int(input())
for _ in range(n):
    x=int(input())
    print(count(x,2))