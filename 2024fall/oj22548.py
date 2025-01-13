a=list(map(int,input().split()))
n=len(a)
profit=0
price=float('inf')
for i in range(n):
    if a[i]<price:
        price=a[i]
    profit=max(a[i]-price,profit)
print(profit)