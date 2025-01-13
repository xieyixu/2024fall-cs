t=int(input())
answer=[]
for _ in range(t):
    n,m,b=map(int,input().split())
    e=[]
    for _ in range(n):
        t,x=map(int,input().split())
        e.append([t,x])
    e.sort(key=lambda x:(x[0],-x[1]))
    count=0
    t=0
    for i in range(n):
        if e[i][0]==t:
            if count<m-1:
                b-=e[i][1]
                count+=1
            else:
                b=b
                count+=1
        else:
            t=e[i][0]
            b-=e[i][1]
            count=0
        if b<=0:
            answer.append(e[i][0])
            break
    if b>0:
        answer.append('alive')
for s in answer:
    print(s)