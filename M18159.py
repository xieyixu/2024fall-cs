T=int(input())
def find_prime(n):
    is_prime = [True] * (n)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(1, n):
        if is_prime[i]:
            k = i
            while i * k <= n - 1:
                is_prime[i * k] = False
                k += 1
    return is_prime
nums=[]
for j in range(T):
    n=int(input())
    nums.append(n)
max_num=max(nums)
is_prime=find_prime(max_num)
for i in range(T):
    answer=[]
    for j in range(nums[i]):
        if is_prime[j]:
            if str(j)[-1]=='1':
                answer.append(j)
    print(f'Case{i+1}:')
    if answer:
        print(' '.join(map(str,answer)))
    else:
        print(f'NULL')