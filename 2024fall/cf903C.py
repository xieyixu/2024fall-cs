from collections import Counter
n=int(input())
a=list(map(int,input().split()))
f=Counter(a)
print(max(f.values()))