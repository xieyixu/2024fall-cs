n=int(input())
nums=list(map(int,input().split()))
all_path=[]
def dfs(index,path):
    path.append(nums[index])
    left=2*index+1
    right=2*index+2
    if left>=n and right>=n:
        all_path.append(path[:])
    else:
        if right<n:
            dfs(right,path)
        if left<n:
            dfs(left,path)
    path.pop()
dfs(0,[])
for path in all_path:
    print(' '.join(map(str,path)))
is_max_heap=True
is_min_heap=True
for i in range(n//2):
    left=2*i+1
    right=2*i+2
    if right<n:
        if nums[i]<nums[right]:
            is_max_heap=False
        if nums[i]>nums[right]:
            is_min_heap=False
if is_max_heap:
   print('Max Heap')
elif is_min_heap:
    print('Min Heap')
else:
    print('Not Heap')