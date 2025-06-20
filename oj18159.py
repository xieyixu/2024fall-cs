import sys
nums=list(map(int,sys.stdin.read().split()))
max_num=max(nums)
queue=[True]*(max_num+1)
queue[0:2]=[False,False]
for i in range(2,int(max_num**0.5)+1):
    if queue[i]:
        queue[i*i::i]=[False]*len(queue[i*i::i])
ans=[]
for i in range(1,len(queue)):
    if queue[i]:
        if str(i)[-1]=='1':
            ans.append(i)
for num in nums:
    res=[]
    for x in ans:
        if x<num:
            res.append(x)
    print(' '.join(map(str,res)))