while True:
    try:
        s=list(input())
        r=[i for i in s]
        n=len(s)
        answer=[' ']*n
        left=[]
        for i in range(n):
            if s[i]=='(':
                left.append(i)
        new_left=reversed(left)
        if new_left:
            for k in new_left:
                for i in range(k+1,n):
                    if s[i]==')':
                        s[k],s[i]='0','0'
                        break
        for i in range(n):
            if s[i]==')':
                answer[i]='?'
            if s[i]=='(':
                answer[i]='$'
        print(''.join(r))
        print(''.join(answer))
    except EOFError:
        break