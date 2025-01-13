n=int(input())
answer=[]
for i in range(n):
    a=input()
    found=False
    if int(a)%19==0:
        found=True
    else:
        for i in range(len(a)-1):
            if a[i]=='1':
                if a[i+1]=='9':
                    found=True
    if found:
        answer.append('Yes')
    else:
        answer.append('No')
for s in answer:
    print(s)