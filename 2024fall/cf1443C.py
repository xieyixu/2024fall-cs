t=int(input())
T=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    dishes=sorted(zip(a,b),key=lambda x:x[0],reverse=True)
    pick_up=0
    delivery=0
    for ai,bi in dishes:
        pick_up+=bi
        d=delivery
        delivery=max(delivery,ai)
        if delivery>pick_up:
            delivery=d
        elif delivery<=pick_up:
            pick_up-=bi
    T.append(max(pick_up,delivery))
for _ in T:
    print(_)