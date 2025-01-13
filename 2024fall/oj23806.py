a=list(map(int,input().split()))
a.sort()
n=len(a)
count=0
result=[]
for i in range(n):
    if i>0 and a[i]==a[i-1]:
        continue
    left,right=i+1,n-1
    while left<right:
        total=a[i]+a[left]+a[right]
        if total==0:
            result.append((a[i],a[left],a[right]))
            right-=1
            left+=1
        elif total>0:
            right-=1
        elif total<0:
            left+=1
result=set(result)   #去重可以使用set

print(len(result))