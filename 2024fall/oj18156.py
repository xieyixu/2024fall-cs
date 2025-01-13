T=int(input())
s=list(map(int,input().split()))
n=len(s)
s.sort()
sum0=float('inf')
right=n-1
left=0
while left<right:
    sum=s[right]+s[left]
    if abs(sum-T)<abs(sum0-T):
        sum0=sum
    elif abs(sum-T)==abs(sum0-T):
        sum0=min(sum,sum0)
    if sum>T:
        right-=1
    elif sum<T:
        left+=1
    elif sum==T:
        break
print(sum0)