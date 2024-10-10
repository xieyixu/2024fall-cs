n=int(input())
T=[]
cube=[i**3 for i in range(n+1)]
for a in range(2,n+1):
    for b in range(2,n):
        for c in range(b,n):
            for d in range(c,n):
                if cube[a]==cube[b]+cube[c]+cube[d]:
                    result=[a,b,c,d]
                    T.append(result)
T.sort()
for t in T:
    print(f"Cube = {t[0]}, Triple = ({t[1]},{t[2]},{t[3]})")