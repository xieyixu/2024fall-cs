n=int(input())
a=list(map(int,input().split()))
m=int(input())
a.sort()
left,right=0,n-1
while left<right:
    if a[left]+a[right]==m:
        print(f'{a[left]} {a[right]}')
        break
    elif a[left]+a[right]<m:
        left+=1
    else:
        right-=1
else:
    print('No')