n=int(input())
b=list(map(int,input().split()))
a=[i-520 for i in b]
prefix=[0]*(n+1)
prefix[0]=0
for i in range(1,n+1):
    prefix[i]=prefix[i-1]+a[i-1]
H={}
max_value=0
for i in range(n+1):
    if prefix[i] in H:
        max_value=max(max_value,(i-H[prefix[i]])*520)
    else:
        H[prefix[i]]=i
print(max_value)