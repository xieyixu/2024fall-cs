n=int(input())
t=[]
for i in range(n):
    a,b=map(int,input().split())
    t.append([a,b])
t.sort(key=lambda x:x[1])
count=1
f=t[0][1]
for i in range(1,n):
    if t[i][0]>f:
        count+=1
        f=t[i][1]
print(count)