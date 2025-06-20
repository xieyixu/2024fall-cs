N,C=map(int,input().split())
a=[]
for i in range(N):
    a.append(int(input()))
a.sort()
def find(a,C):
    low,high=1,a[-1]-a[0]
    while low<=high:
        mid=(low+high)//2
        i=0
        current=a[0]
        count=1
        while i<N:
            if a[i]-current>=mid:
                count+=1
                current=a[i]
            i+=1
        if count>=C:
            low=mid+1
        else:
            high=mid-1
    return high
s=find(a,C)
print(s)