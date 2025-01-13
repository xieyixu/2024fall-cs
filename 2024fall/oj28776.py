n=int(input())
a0,b0=map(int,input().split())
s=[]
for _ in range(n):
    a,b=map(int,input().split())
    s.append([a,b])
s_sorted=sorted(s,key=lambda x:x[0]*x[1])
max_money=0
k=a0
for i in range(n):
    a,b=s_sorted[i][0],s_sorted[i][1]
    max_money=max(max_money,k//b)
    k*=a
print(max_money)