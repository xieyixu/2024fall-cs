import sys

data=sys.stdin.read().splitlines()
n,m=map(int,data[0].split())
a=list(map(int,data[1].split()))
dp=[0]*(n)
dp[n-1]=1
b=set()
b.add(a[n-1])

for i in range(n-2,-1,-1):
        if a[i] not in b:
            dp[i]=dp[i+1]+1
            b.add(a[i])
        else:
            dp[i]=dp[i+1]

l=[int(data[i]) for i in range(2,m+2)]

results = [dp[q - 1] for q in l]
print('\n'.join(map(str, results)))