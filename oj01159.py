n=int(input())
s=list(map(str,input()))
prev=[0]*n
for i in range(n-1,-1,-1):
    curr=[0]*n
    curr[i]=1
    if i<n-1:
        curr[i+1]=2 if s[i]==s[i+1] else 1
    for j in range(i+2,n):
        if s[i]==s[j]:
            curr[j]=prev[j-1]+2
        else:
            curr[j]=max(prev[j],curr[j-1])
    prev=curr
print(n-prev[-1])