N,M=map(int,input().split())
answer=0
stack=[(1,False),(1,True)]
count=0
while stack:
    x,bool=stack.pop()
    if bool:
        count+=1
        if 1<=x<N:
            if count<M-1:
                stack.append((x+1,False))
                stack.append((x+1,True))
            elif count==M-1:
                stack.append((x+1,False))
        elif x==N:
            answer+=1
    else:
        count=0
        if 1<=x<N:
            stack.append((x+1,False))
            stack.append((x+1,True))
        elif x==N:
            answer+=1
print(answer)#使用DFS会超时，必须要dp或者结合记忆化搜索。