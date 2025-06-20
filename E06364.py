N,K=map(int,input().split())
d=[]
for i in range(N):
    a,b=map(int,input().split())
    d.append((a,b,i+1))
d.sort(reverse=True)
s=d[:K]
s.sort(key=lambda x:x[1],reverse=True)
print(s[0][2])