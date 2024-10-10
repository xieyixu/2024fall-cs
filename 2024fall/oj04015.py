def validate_email(email):
    f=0
    g=0
    a=0
    if email[0]=='@' or email[0]=='.' or email[-1]=='@' or email[-1]=='.':
        print('NO')
    else:
        for i in range(len(email)):
            if email[i]=='@':
                f=f+1
                a=i

        if f!=1:
            print('NO')
        else:
            for i in range(a,len(email)):
                if email[i]=='.':
                    g=g+1
            if g!=0:
                if email[a+1]=='.' or email[a-1]=='.':
                    print('NO')
                else:
                    print('YES')
            else:
                print('NO')


try:
    while True:
        email = input().strip()
        if not email:
            continue
        validate_email(email)
except EOFError:
    pass