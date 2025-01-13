from collections import deque
while True:
    try:
        m=input()
        n=len(m)
        a=int(m)
        k=deque(m)
        i=0
        find=True
        t0=[j for j in range(1,n+1)]
        t1=[]
        while i<n:
            k.append(k.popleft())
            d=int(''.join(k))
            if d%a!=0 or not (1<=d//a<=n):
                find=False
                break
            else:
                t1.append(d//a)
            i+=1
        if set(t1)==set(t0):
            find=True
        else:
            find=False
        if find:
            print(f'{m} is cyclic')
        else:
            print(f'{m} is not cyclic')
    except EOFError:
        break