T=[]
while True:
    R,n=map(int,input().split())
    if R==-1 and n==-1:
        break
    else:
        x=list(map(int,input().split()))
        x.sort()
        t=1
        max=x[0]
        min=x[0]
        for i in range(len(x)):
            if x[i]-min<=R:
                max=x[i]
            elif x[i]-max<=R:
                t=t
            else:
                t+=1
                min=x[i]
                max=x[i]
        T.append(t)
for t in T:
    print(t)