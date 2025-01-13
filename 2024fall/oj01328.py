from math import sqrt
a=[]
while True:
    line=input().strip()
    if not line:
        continue
    n,d=map(int,line.split())
    if n==0 and d==0:
        break
    else:
        found=True
        T=[]
        for _ in range(n):
            x,y=map(int,input().split())
            if y>d or d<0:
                found=False
            else:
                T.append([x-sqrt(d**2-y**2),x+sqrt(d**2-y**2)])
        if found:
            T.sort(key=lambda x:x[1])
            i=0
            b=0
            t=1
            while i<n:
                if T[i][0]<=T[b][1]:
                    i+=1
                else:
                    t+=1
                    b=i
                    i+=1
            a.append(t)
        else:
            a.append(-1)

for i in range(len(a)):
    print(f"Case {i+1}: {a[i]}")