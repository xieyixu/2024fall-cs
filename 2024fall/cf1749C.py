from collections import deque
def number_game(a,k):
    i=1
    b=[s for s in a if s<=k]
    b.sort()
    b=deque(b)
    if len(b)<2*k-1:
        return False
    while i<=k:
        while b and b[-1]>k-i+1:
            b.pop()
        if not b:
            return False
        b.pop()
        if b:
            b.popleft()
        i+=1
    return True


t=int(input())
K=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    k=0
    while number_game(a,k):
        k+=1
    K.append(k-1 if k!=0 else 0)
for k in K:
    print(k)