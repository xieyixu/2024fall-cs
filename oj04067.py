while True:
    try:
        n=input()
        m=''.join(reversed(list(n)))
        if m==n:
            print('YES')
        else:
            print('NO')
    except EOFError:
        break