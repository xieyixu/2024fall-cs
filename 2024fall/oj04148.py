T=[]

while True:
    p,e,i,d=map(int,input().split())
    if p==-1 and e==-1 and i==-1 and d==-1:
        break
    else:
        t=d+1
        while t<=21252+d:
            if (t-p)%23==0 and (t-e)%28==0 and (t-i)%33==0:
                T.append(t-d)
                break
            t+=1

for i in range(len(T)):
    print(f"Case {i+1}: the next triple peak occurs in {T[i]} days.")