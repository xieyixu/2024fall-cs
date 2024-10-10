n,l=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
t=[]
if n!=1:
    for i in range(len(a)-1):
        t.append(a[i+1]-a[i])
    T=max(t)/2
    print(f"{max(T,a[0],l-a[n-1]):.10f}")
else:
    print(f"{max(a[0],l-a[0]):.10f}")