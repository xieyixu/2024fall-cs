n,K=map(int,input().split())
a=[]
while n>0:
    if n%K<10:
        t=n%K
        a.append(t)
    elif n%K==10:
        a.append('A')
    elif n%K==11:
        a.append('B')
    elif n%K==12:
        a.append('C')
    elif n%K==13:
        a.append('D')
    elif n%K==14:
        a.append('E')
    elif n%K==15:
        a.append('F')
    n//=K
a.reverse()
for x in a:
    print(f"{x}",end='')