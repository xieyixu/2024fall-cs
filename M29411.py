n=int(input())
answer=[]
a1=n//1000
n=n-a1*1000
answer.append('M'*a1)
a2=n//100
n=n-a2*100
if a2==9:
    answer.append('CM')
elif a2==4:
    answer.append('CD')
else:
    if a2>=5:
        answer.append('D'+'C'*(a2-5))
    else:
        answer.append('C'*a2)
a3=n//10
n=n-a3*10
if a3==9:
    answer.append('XC')
elif a3==4:
    answer.append('XL')
else:
    if a3>=5:
        answer.append('L'+'X'*(a3-5))
    else:
        answer.append('X'*a3)
a4=n
if a4==9:
    answer.append('IX')
elif a4==4:
    answer.append('IV')
else:
    if a4>=5:
        answer.append('V'+'I'*(a4-5))
    else:
        answer.append('I'*a4)
print(''.join(answer))