def Hanoi_3(m):
    return 2**(m)-1
check={}
def Hanoi_4(n):
    min_moves=[0]*(n+1)
    min_moves[1]=1
    if n>2:
        min_moves[2]=3
    for k in range(3, n+1):
        min_moves[k]=float('inf')
        for i in range(1,k):
            movement=2*min_moves[i]+Hanoi_3(k-i)
            min_moves[k]=min(min_moves[k],movement)  #并没有用到递归
    return min_moves

for _ in range(1,13):
    print(Hanoi_4(12)[_])

#递归似乎不行，超出限制，应该还是要dp。