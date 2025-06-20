t=int(input())
for _ in range(t):
    n,k_1=input().split()
    k=int(k_1)
    stack=[]
    for digit in n:
        while k and stack and stack[-1]>digit:
            stack.pop()
            k-=1
        stack.append(digit)
    while k:
        stack.pop()
        k-=1
    print(''.join(stack))