n=int(input())
values=list(map(int,input().split()))
choose = [0] * (n + 1)
no_choose = [0] * (n + 1)
for i in range(n, 0, -1):
    left = 2 * i
    right = 2 * i + 1
    left_yes = choose[left] if left <= n else 0
    left_no = no_choose[left] if left <= n else 0
    right_yes = choose[right] if right <= n else 0
    right_no = no_choose[right] if right <= n else 0
    choose_val = values[i - 1] + left_no + right_no
    no_val = max(left_yes, left_no) + max(right_yes, right_no)
    choose[i] = choose_val
    no_choose[i] = no_val
print(max(choose[1], no_choose[1]))