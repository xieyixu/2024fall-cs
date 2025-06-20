n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    left,right=0,0
    while a!=1 or b!=1:
        if a>b:
            k=(a-1)//b
            left+=k
            a-=k*b
        elif b>a:
            k=(b-1)//a
            right+=k
            b-=k*a
    print(f'Scenario #{i+1}:')
    print(f'{left} {right}')
    print()