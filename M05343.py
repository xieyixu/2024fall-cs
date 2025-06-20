n=int(input())
letters={'A':0,'B':1,'C':2,'D':3}
nums={0:'A',1:'B',2:'C',3:'D'}
queue_1=list(map(str,input().split()))
d1={i:[] for i in range(9)}
for x in queue_1:
    i=int(x[1])-1
    d1[i].append(x)
queue_2=[]
for i in range(9):
    print(f'Queue{i+1}:',end='')
    if d1[i]:
        print(' '.join(d1[i]))
    else:
        print()
for i in range(9):
    while d1[i]:
        x=d1[i].pop()
        queue_2.append(x)
d2={i:[] for i in range(4)}
for x in queue_2:
    y=x[0]
    d2[letters[y]].append(x)
for i in range(4):
    print(f'Queue{nums[i]}:',end='')
    if d2[i]:
        print(' '.join(d2[i]))
queue_1.sort()
print(' '.join(queue_1))