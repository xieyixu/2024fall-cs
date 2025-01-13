def generate(s):
    all=[]
    if len(s)==0:
        return [[]]
    for i in range(len(s)):
        current=s[i]
        remain=s[:i]+s[i+1:]
        for perm in generate(remain):
            all.append([current]+perm)
    return all

n=int(input())
s=[i for i in range(1,n+1)]
all=generate(s)
for j in all:
    for i in j:
        if i!=j[-1]:
            print(i,end=' ')
        else:
            print(i)