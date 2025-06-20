a=int(input())
answer=[]
while a>0:
    answer.append(a%8)
    a=a//8
print(''.join(map(str,reversed(answer))))
