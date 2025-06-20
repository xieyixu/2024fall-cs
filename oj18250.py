while True:
    try:
        n,m=map(int,input().split())
        parent=list(range(n+1))
        def find(u):
            while parent[u]!=u:
                parent[u]=parent[parent[u]]
                u=parent[u]
            return u
        for _ in range(m):
            x,y=map(int,input().split())
            find_x=find(x)
            find_y=find(y)
            if find_x!=find_y:
                print('No')
                parent[find_y] = find_x
            else:
                print('Yes')
        roots=set()
        for i in range(1,n+1):
            roots.add(find(i))
        roots=sorted(roots)
        print(len(roots))
        print(' '.join(map(str,roots)))
    except EOFError:
        break