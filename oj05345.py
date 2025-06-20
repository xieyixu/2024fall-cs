N,M=map(int,input().split())
a=list(map(int,input().split()))
c=[]
for _ in range(M):
    c.append(list(input().split()))
for i in range(M):
    a1,a2=c[i]
    if a1=='C':
        for i in range(N):
            a[i]=(a[i]+int(a2))%66351
    elif a1=='Q':
        count=0
        for i in range(N):
            k=str(bin(a[i])[2:].zfill(16))[::-1]
            if k[int(a2)]!='0':
                count+=1
        print(count)