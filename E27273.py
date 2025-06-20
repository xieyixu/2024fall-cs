t=int(input())
for _ in range(t):
    n=int(input())
    i=0
    nums_2=[]
    while 2**i<=n:
        nums_2.append(2**i)
        i+=1
    ans=0
    for i in range(1,n+1):
        if i in nums_2:
            ans-=i
        else:
            ans+=i
    print(ans)