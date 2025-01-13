n=int(input())
a=list(input().split())
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]+a[j]<a[j]+a[i]:
            a[i],a[j]=a[j],a[i]
ans1="".join(a)
a.reverse()
ans2="".join(a)
print(ans1+" "+ans2)