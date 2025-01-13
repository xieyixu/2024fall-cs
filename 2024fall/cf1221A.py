def can_win_with_2048(s):
    total_sum = sum(x for x in s if x <= 2048)
    return total_sum >= 2048
q=int(input())
T=[]
for i in range(q):
    n=int(input())
    s=list(map(int,input().split()))
    if can_win_with_2048(s):
        T.append(True)
    else:
        T.append(False)
for t in T:
    if t:
        print("YES")
    else:
        print("NO")