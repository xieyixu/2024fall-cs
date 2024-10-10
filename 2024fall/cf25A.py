n=int(input())
numbers=list(map(int,input().split()))
j=0
evenness=[]
while j<n:
    even=numbers[j]%2
    evenness.append(even)
    j+=1
i=0
while i<n:
    if evenness[i]==evenness[i+1]:
        i+=1
    elif evenness[i]!=evenness[i+1]:
        if evenness[i]==evenness[i-1]:
            print(i+2)
            break
        elif evenness[i]!=evenness[i-1]:
            print(i+1)
            break