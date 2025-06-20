n=int(input())
def stack(n):
    if n <= 1:
        return 1
    total = 0
    for k in range(n):
        total += stack(k) * stack(n-1-k)
    return total
print(stack(n))