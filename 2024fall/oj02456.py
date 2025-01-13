N,C=map(int,input().split())
a=[]
for i in range(N):
    n=int(input())
    a.append(n)
a.sort()

def place_cows(d):
    count=1
    last_position=a[0]
    for i in range(1,N):
        if a[i]-last_position>=d:
            count+=1
            last_position=a[i]
            if count==C:
                return True
    return False

left,right=a[0],a[-1]-a[0]
distance=0
while left<=right:
    mid=(left+right)//2
    if place_cows(mid):
        distance=mid
        left=mid+1
    else:
        right=mid-1
print(distance)