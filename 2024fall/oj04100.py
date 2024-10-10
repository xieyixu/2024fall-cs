def test(P):   #合理利用函数和贪心算法
    tests=[]
    for s,d in P:
        if not tests or s>tests[-1]:
            tests.append(d)
    return len(tests)

k=int(input())
T=[]
for _ in range(k):
    n=int(input())
    P=[]
    for i in range(n):
        p=list(map(int,input().split()))
        P.append(p)
    P=sorted(P,key=lambda x:(x[1],x[0]))
    t=test(P)
    T.append(t)
for t in T:
    print(t)