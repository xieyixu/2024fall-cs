n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
s=sum(a)
while True:
    if a[-1]>s/k:
        s-=a.pop()
        k-=1
    else:
        print(f'{s/k:.3f}')
        break