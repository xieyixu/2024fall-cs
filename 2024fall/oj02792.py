from collections import Counter
n=int(input())
T=[]
for _ in range(n):
    s=int(input())
    n1=int(input())
    A=list(map(int,input().split())) #超时时使用集合或字典来代替列表，元素要考虑重复就用字典，不要考虑重复就用集合。集合与字典比列表快许多
    n2=int(input())
    B=list(map(int,input().split()))#这里可以用两个集合，A，B都计数，会更快。
    t=0
    B_Count=Counter(B)
    for p in A:
        if s-p in B_Count:
            t+=B_Count[s-p]
    T.append(t)
for t in T:
    print(t)