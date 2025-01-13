from collections import defaultdict
from itertools import permutations
a = defaultdict(int)
b = defaultdict(int)
c = defaultdict(int)
d = defaultdict(int)
n = int(input())
for i in input():
    a[i] += 1
for i in input():
    b[i] += 1
for i in input():
    c[i] += 1
for i in input():
    d[i] += 1
dicts = [a, b, c, d]
def check(word):
    for perm in permutations(dicts, len(word)):    #这是一个语法题，重点就是直接生成所有的可能的排列组合。
        for i, d in enumerate(perm):
            print(i,d)
            if word[i] not in d:
                break   #只跳出当前这个循环，不会跳出上一个循环
        else:
            return 'YES'    #只要有一次被成功匹配，就会执行
    else:
        return 'NO'
for _ in range(n):
    word = input()
    print(check(word))