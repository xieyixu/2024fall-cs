n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))   #定义两个dp
dp1=[0]*(n+1)
dp2=[0]*(n+1)
for i in range(1,n+1):
    dp1[i]=max(dp1[i-1],dp2[i-1]+a[i-1])
    dp2[i]=max(dp1[i-1]+b[i-1],dp2[i-1])
print(max(dp1[n],dp2[n]))