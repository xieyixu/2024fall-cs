q=int(input())
p=list(map(int,input().split()))
t1=0
t2=0
while True:
    if p:
        min_p=min(p)
        max_p=max(p)
        if q>=min_p:
            q=q-min_p
            p.remove(min_p)
            t1+=1
        elif q<min_p:   #使用if会报错。使用if的话，会直接执行这个程序，而不会更新min和max的数值。
            if len(p)!=1 and t1>t2:
                q=q+max_p
                p.remove(max_p)
                t2+=1
            elif len(p)==1:
                break
            else:
                break
    else:
        break
print(t1-t2)