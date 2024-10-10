a=int(input())
mu=1
if a==1:
    mu=1
for s in range(2,int(a**0.5)+1,1):
    if a%(s*s)==0:
        mu=0
        break
for s in range(2,int(a**0.5)+1,1):
    while a % s == 0:
        mu=mu*(-1)
        a //= s
if a>2:
    mu=mu*(-1)
print(mu)