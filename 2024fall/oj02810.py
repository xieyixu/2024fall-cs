n=int(input())
T=[]
for a in range(2,n+1):
    for b in range(2,a):
        for c in range(b,a):
            for d in range(c,a):
                if a**3-b**3-c**3-d**3==0:
                    t=[a,b,c,d]
                    T.append(t)
T.sort()
for t in T:
    print(f"Cube = {t[0]}, Triple = ({t[1]},{t[2]},{t[3]})")    #应该要用字符串格式化