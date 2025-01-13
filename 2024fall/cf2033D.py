t=int(input())
answers=[]

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    prefix_sum=0
    prefix_map=set()
    prefix_map.add(0)
    count=0
    for i in range(n):
        prefix_sum+=a[i]
        if prefix_sum in prefix_map:
            count+=1
            prefix_map.clear()
            prefix_map.add(0)
            prefix_sum = 0
        else:
            prefix_map.add(prefix_sum)
    answers.append(count)
for answer in answers:
    print(answer)