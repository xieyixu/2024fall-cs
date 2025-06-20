x=5

while True:
    f = x ** 3 - 5 * x ** 2 + 10 * x - 80
    diff_f = 3 * x ** 2 - 10 * x + 10
    delta_x=-f/diff_f
    x=x+delta_x
    if x ** 3 - 5 * x ** 2 + 10 * x - 80<1e-9:
        break
print(f'{x:.9f}')