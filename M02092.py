from collections import defaultdict
while True:
    N,M=map(int,input().split())
    if N==0 and M==0:
        break
    board=[]
    for i in range(N):
        board+=list(map(int,input().split()))
    dictionary=defaultdict(int)
    for num in board:
        if num not in dictionary:
            dictionary[num]=1
        else:
            dictionary[num]+=1
    sorted_dictionary=sorted(dict(dictionary).items(),key=lambda x:x[1],reverse=True)
    second_result=sorted(set(sorted_dictionary),key=lambda x:x[1],reverse=True)[1][1]
    answer = [v for v, k in sorted_dictionary if k == second_result]
    print(' '.join(map(str,sorted(answer))))
