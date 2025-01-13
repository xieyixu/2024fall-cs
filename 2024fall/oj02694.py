def polish(s):
    def take(expr):
        token=expr.pop(0)
        if token=='+':
            left=take(expr)
            right=take(expr)
            return left+right
        elif token=='-':
            left=take(expr)
            right=take(expr)
            return left-right
        elif token=='*':
            left=take(expr)
            right=take(expr)
            return left*right
        elif token=='/':
            left=take(expr)
            right=take(expr)
            return left/right
        else:
            return float(token)
    return take(s[:])

s=list(input().split())
print(f'{polish(s):.6f}')