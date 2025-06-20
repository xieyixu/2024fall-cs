import math
while True:
    try:
        x,y=map(int,input().split())
        print(math.gcd(x,y))
    except EOFError:
        break