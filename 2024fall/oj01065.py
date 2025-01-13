from bisect import bisect_left
t=int(input())
answer=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[[a[i],a[i+1]] for i in range(0,2*n,2)]
    b.sort(key=lambda x:(x[0],x[1]))   #首先按照长度排，长度相同再按照重量排，找递增子序列时l就已经排好了。
    lis=[]
    weight=[w for l,w in b]   #反转重量找最长不递减子序列。
    weight.reverse()
    for w in weight:
        pos=bisect_left(lis,w)    #二分查找
        if pos>=len(lis):
            lis.append(w)
        else:
            lis[pos]=w
    answer.append(len(lis))
for s in answer:
    print(s)