from collections import deque
t=int(input())
T=[]
for i in range(t):
    n,x=map(int,input().split())
    a=deque(map(int,input().split()))
    b=a.copy()  #a=b只是一个引用，要重新弄一个得用copy（）。
    t1=-1
    t2=-1
    total_sum=sum(a)
    while a:
        if total_sum%x!=0:
            t1=len(a)
            break
        total_sum-=a.pop()
    total_sum=sum(b)
    while b:
        if total_sum%x!=0:
            t2=len(b)
            break
        total_sum-=b.popleft()  #最终只要从一边去除就可以了
    T.append(max(t1,t2))
for t in T:
    print(t)