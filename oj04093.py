from collections import defaultdict
N=int(input())
dictionary=defaultdict(set)
for i in range(N):
    l=list(map(int,input().split()))
    c=l[0]
    k=l[1:]
    for x in k:
        dictionary[x].add(i)
M=int(input())
for _ in range(M):
    answer=[]
    l=list(map(int,input().split()))
    for idx,s in dictionary.items():
        valid=True
        for i in range(N):
            condition=l[i]
            if condition==1:
                if i not in s:
                    valid=False
                    break
            elif condition==-1:
                if i in s:
                    valid=False
                    break
        if valid :
            answer.append(idx)
    if answer:
        answer.sort()
        print(' '.join(map(str,answer)))
    else:
        print('NOT FOUND')