import bisect
n=int(input())
x=list(map(int,input().split()))
q=int(input())
m=[int(input()) for i in range(q)]
T=[]
x.sort()
for i in range(q):
    t = bisect.bisect_right(x, m[i])     #采用二分查找可以提高效率
    print(t)