from bisect import bisect_left, bisect_right

nums=list(map(int,input().split()))
target=int(input())
index_1=bisect_left(nums,target)
index_2=bisect_right(nums,target)
if index_1<len(nums) and nums[index_1]==target:
    print(index_1,index_2-1)
else:
    print(-1,-1)