a=list(map(int,input().split()))
n=len(a)
if n==1:
    print(1)
elif n==2:
    if a[0]==a[1]:
        print(1)
    else:
        print(2)
else:
    count=1
    middle_end=0
    for i in range(1,n):
        diff=a[i]-a[i-1]
        if diff>0 and middle_end<=0:
            count+=1
            m=1
        elif diff<0 and middle_end>=0:
            count+=1
            m=-1
    print(count)