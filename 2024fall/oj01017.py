import math
T=[]
while True:
    a,b,c,d,e,f=map(int,input().split())
    t1,t2,t3,t4,t5,t6=0,0,0,0,0,0
    if a==0 and b==0 and c==0 and d==0 and e==0 and f==0:
        break
    else:
        t6=f
        a=max(0,a-11*e)
        t5=e
        t4=d
        if b>=5*d:
            a=a
            b=b-5*d
        else:
            a=max(0,a-(5*d-b)*4)
            b=0
        if c%4==0:
            t3=c/4
            t2=math.ceil((4*b+a)/36)
            t1=0
        else:
            t3=math.floor(c/4)
            if c%4==1:
                b=max(0,b-5)
                t2=1+math.ceil(b/9)
                if b%9!=0:
                    a=max(0,a-7-(36-4*(b%9)))
                elif b%9==0:
                    a=max(0,a-7)
                t1=math.ceil(a/36)
            elif c%4==2:
                b=max(b-3,0)
                t2=1+math.ceil(b/9)
                if b%9!=0:
                    a=max(0,a-6-(36-4*(b%9)))
                elif b%9==0:
                    a=max(0,a-6)
                t1=math.ceil(a/36)
            elif c%4==3:
                b=max(0,b-1)
                t2=1+math.ceil(b/9)
                if b%9!=0:
                    a=max(0,a-5-(36-4*(b%9)))
                elif b%9==0:
                    a=max(0,a-5)
                t1=math.ceil(a/36)
    t=t1+t2+t3+t4+t5+t6
    T.append(t)
for t in T:
    print(int(t))