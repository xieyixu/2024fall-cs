from  math import ceil
H,L,n=map(int,input().split())
v=list(map(int,input().split()))
a=ceil((n)/2)
t=[L/v[i] for i in range(n)]
t.sort()
t0=t[a-1]
if 0.5*10*(t0**2)>H:
    print(f'{0:.2f}')
else:
    h=H-0.5*10*(t0**2)
    print(f'{h:.2f}')