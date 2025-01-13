t=int(input())
numbers=[int(input()) for _ in range(t)]
answer=[]
for number in numbers:
    value=int((number+1)*number*0.5)
    i=0
    while 2**i<=number:
        value-=2*(2**i)
        i+=1
    answer.append(value)
for s in answer:
    print(s)