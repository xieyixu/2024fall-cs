m,c=map(int,input().split())
events=[]
for _ in range(m):
    n,s,d=map(int,input().split())
    events.append((s,1,n))
    events.append((s+d,0,n))
events.sort(key=lambda x:x[0])
found=True
for event in events:
    if event[1]==1:
        c-=event[2]
        if c<0:
            print('N')
            found=False
            break
    elif event[1]==0:
        c+=event[2]
if found:
    print('Y')