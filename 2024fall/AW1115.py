while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    if a<b:
        a,b=b,a
    i=0
    while a//b<2 and a!=b:
        a,b=b,a-b
        i+=1
    if i%2==0:
        print('win')
    else:
        print('lose')