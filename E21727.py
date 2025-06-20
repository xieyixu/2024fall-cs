N,M=map(int,input().split())
nums=list(map(int,input().split()))
prefix=[0]*(N+1)
s=0
for i in range(1,N+1):
    prefix[i]=prefix[i-1]+nums[i-1]
    if prefix[i]<=M:
        s=i
    else:
        break
print(s)