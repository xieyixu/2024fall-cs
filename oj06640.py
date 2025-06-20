from collections import defaultdict
N=int(input())
dictionary=defaultdict(list)
for j in range(N):
    l=input().split()
    c=int(l[0])
    words=l[1:c+1]
    words=set(words)
    for word in words:
        dictionary[word].append(j+1)
M=int(input())
for _ in range(M):
    word=input().strip()
    if dictionary[word]:
        print(' '.join(map(str,dictionary[word])))
    else:
        print('NOT FOUND')