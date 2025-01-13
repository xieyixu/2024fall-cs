s=input()
n=len(s)
dp_1=[0]*n
dp_2=[0]*n
if s[0]=='R':
    dp_2[0]=1
if s[0]=='B':
    dp_1[0]=1
for i in range(1,n):
    if s[i]=='R':
        dp_1[i]=min(dp_2[i-1]+1,dp_1[i-1])
        dp_2[i]=min(dp_2[i-1]+1,dp_1[i]+1)
    if s[i]=='B':
        dp_2[i]=min(dp_1[i-1]+1,dp_2[i-1])
        dp_1[i]=min(dp_2[i]+1,dp_1[i-1]+1)
print(dp_1[n-1])