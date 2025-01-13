from collections import deque
N,D=map(int,input().split())
F=deque(int(input()) for _ in range(N))
M=[]

while F:
    inlist=[]
    max=F[0]
    min=F[0]
    for _ in range(len(F)):
        h=F.popleft()
        if abs(h-max)<=D and abs(h-min)<=D:
            inlist.append(h)
        else:
            F.append(h)
        if h>max:
            max=h
        if h<min:
            min=h
    M+=sorted(inlist)
for m in M:
    print(m)