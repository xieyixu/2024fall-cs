n=int(input())
for i in range(1,n+1):
    if i==1:
        print('*')
    elif i==2:
        print('**')
    elif i==n:
        for _ in range(n):
            print('*',end='')
    else:
        for j in range(i):
            if j==0:
                print('*',end='')
            elif j==i-1:
                print('*')
            else:
                print(' ',end='')