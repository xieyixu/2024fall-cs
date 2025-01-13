n=int(input())
computer_write=[]
for _ in range(n):
    c,w=map(int,input().split())
    computer_write.append((c,w))
computer_write.sort(key=lambda x:(-x[1],x[0]))
total_time=0
computer_time=0
for i in range(n):
    computer_time+=computer_write[i][0]
    total_time=max(total_time,computer_time+computer_write[i][1])
print(total_time)