def lucky_number(n):
    for s in str(n):
        if s!='7' and s!='4':
            return False
    return True

a=int(input())
if lucky_number(a):
    print("YES")
else:
    for i in range(a):
        if lucky_number(i):
            if a%i==0:
                print("YES")
                break
    else:
        print("NO")