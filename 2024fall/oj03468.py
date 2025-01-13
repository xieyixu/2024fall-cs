while True:
    try:
        N=int(input())
        t=list(map(int,input().split()))
        sum_t=sum(t)
        t.sort()
        t_final=sum_t/2
        while t and t[-1]>t_final:
            k=t.pop()
            sum_t-=k
            t_final=sum_t
        print(f'{t_final:.1f}')
    except EOFError:
        break