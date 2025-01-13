n=int(input())
a=list(map(int,input().split()))
results=[]
def dfs(x,path):
    path.append(a[x])
    l,r=2*x+1,2*x+2
    if l>=n and r>=n:
        results.append(path)
    else:
        if r<n:
            dfs(r,path[:])
        if l<n:
            dfs(l,path[:])
    return results
dfs(0,[])
find=True
for result in results:
    print(' '.join(map(str,result)))
    if sorted(result)!=result and sorted(result,reverse=True)!=result:
        find=False
if not find:
    print('Not Heap')
else:
    if sorted(results[0])==results[0]:
        print('Min Heap')
    elif sorted(results[0],reverse=True)==results[0]:
        print('Max Heap')