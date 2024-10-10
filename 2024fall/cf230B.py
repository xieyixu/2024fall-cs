import math
def prime(a):
    primes=[True]*(a+1)
    p=2
    for p in range(2,int(math.sqrt(a))+1):
        if primes[p]:
            for i in range(p*p,a+1,p):
                primes[i]=False
    prime_list=list(p for p in range(2,a+1) if primes[p])
    return prime_list                #埃氏筛，生成质数列表。

n=int(input())
a=list(map(int,input().split()))
primes=prime(10**6)             #在列表中找一个数可能会比较慢，不如直接生成
T_prime={p*p for p in primes}      #用集合会比用列表更快
for number in a:
    if number in T_prime:
        print("YES")
    else:
        print("NO")