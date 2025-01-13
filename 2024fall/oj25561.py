from itertools import product
n,m=map(int,input().split())
a=[[float('inf')]*m for _ in range(n)]
b=[[] for _ in range(m)]
for i in range(n):
    data=input().split()
    for j in range(len(data)):
        s,p=map(int,data[j].split(':'))
        a[i][s-1]=p
for i in range(m):
    data=input().split()
    for j in range(len(data)):
        q,x=map(int,data[j].split('-'))
        b[i].append((q,x))
def kuadiandazhe(total_price):
    return (total_price//300)*50
def youhuiquan(total_price,coupons):
    best_price=total_price
    for coupon in coupons:
        q,x=coupon
        if total_price>=q:
            best_price=min(best_price,total_price-x)
    return best_price
def min_total_price(n,m,prices,coupons):
    min_price=float('inf')
    for choice in product(*[range(m) for _ in range(n)]):
        total_price=0
        shop_price=[0]*m
        for i in range(n):
            store_idx=choice[i]
            price=prices[i][store_idx]
            total_price+=price
            shop_price[store_idx]+=price
        for j in range(m):
            if shop_price[j]>0:
                shop_price[j]=youhuiquan(shop_price[j],coupons[j])
        min_price=min(min_price,sum(shop_price)-kuadiandazhe(total_price))
    return min_price
print(min_total_price(n,m,a,b))