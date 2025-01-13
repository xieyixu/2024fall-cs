def count_unique_numbers():
    n = int(input())
    numbers = []
    for _ in range(n):
        num = int(input())
        numbers.append(num)

    unique_numbers = set(numbers)
    print(len(unique_numbers))


count_unique_numbers()