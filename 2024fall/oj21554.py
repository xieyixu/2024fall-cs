n=int(input())
t=list(map(int,input().split()))
T=[[i,t[i]]  for i in range(n)]
T.sort(key=lambda x:x[1])
average=sum(T[i][1]*(n-i-1) for i in range(n))/n
for i in range(n):
    print(T[i][0]+1,end=' ')
print()
print(f"{average:.2f}")