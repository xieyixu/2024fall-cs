n=int(input())
i=0
x=0
program=[]
while i<n:
    s=input()
    program.append(s)
    i+=1
j=0
while j<n:
    if program[j]=='++X' or program[j]=='X++':
        x=x+1
    elif program[j]=='--X' or program[j]=='X--':
        x=x-1
    j+=1
print(x)