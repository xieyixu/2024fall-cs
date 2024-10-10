# Assignment #2: 语法练习

Updated 0126 GMT+8 Sep 24, 2024

2024 fall, Complied by ==曾弘倓  物理学院  2400011513==



## 1. 题目

### 263A. Beautiful Matrix

https://codeforces.com/problemset/problem/263/A



思路：



##### 代码

```python
beautiful_matrix=[]
for i in range(5):
    bm=list(map(int,input().split()))
    beautiful_matrix.append(bm)

for i in range(5):
    for j in range(5):
        if beautiful_matrix[i][j]==1:
            print(abs(i-2)+abs(j-2))

```



代码运行截图 ====

![image-20240925155746008](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240925155746008.png)



### 1328A. Divisibility Problem

https://codeforces.com/problemset/problem/1328/A



思路：



##### 代码

```python
n=int(input())
numbers=[]
for i in range(n):
    a=list(map(int,input().split()))
    numbers.append(a)
for i in range(n):
    a,b=numbers[i][0],numbers[i][1]
    if a%b!=0:
        print(b-(a%b))
    elif a%b==0:
        print(0)
```



代码运行截图 ====

![image-20240925155857596](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240925155857596.png)



### 427A. Police Recruits

https://codeforces.com/problemset/problem/427/A



思路：



##### 代码

```python
n=int(input())
numbers=list(map(int,input().split()))
s=0
t=0
for i in range(n):
    if s>0:
        if numbers[i]<0:
            s=s+numbers[i]
        else:
            s=s+numbers[i]
    elif s<=0:
        if numbers[i]>0:
            s=s+numbers[i]
        else:
            s=s
            t=t+1
print(t)

```



代码运行截图 ====

![image-20240925160048987](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240925160048987.png)



### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：



##### 代码

```python
def count_remaining_trees(L, M, regions):
    removed = [False] * (L + 1)
    for start, end in regions:
        for i in range(start, end + 1):
            removed[i] = True
    return sum(1 for is_removed in removed if not is_removed)

L, M = map(int, input().split())
regions = [tuple(map(int, input().split())) for _ in range(M)]

remaining_trees = count_remaining_trees(L, M, regions)
print(remaining_trees)

```



代码运行截图 ====

![image-20240925160304090](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240925160304090.png)



### sy60: 水仙花数II

https://sunnywhy.com/sfbj/3/1/60



思路：



##### 代码

```python
def narcissus(n):
    numbers=[int(d) for d in str(n)]
    s=sum(number**3 for number in numbers)
    if s==n:
        return True

a,b=map(int,input().split())
j=0
numbers=[]
for i in range(a,b+1):
    if narcissus(i):
        numbers.append(i)
        j+=1
if j!=0:
    print(' '.join(map(str,numbers)))
elif j==0:
    print("NO")

```



代码运行截图 ====

![image-20240925160535864](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240925160535864.png)



### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/



思路：



##### 代码

```python
import math
t=[]
while True:
    n=int(input())
    if n!=0:
        students=[]
        for i in range(n):
            student=list(map(int,input().split()))
            students.append(student)
        times=[]
        for i in range(n):
            if students[i][1]>=0:
                time=students[i][1]+math.ceil((4.5/(students[i][0]))*3600)
                times.append(time)
        t.append(min(times))
    if n==0:
        break

for time in t:
    print(time)

```



代码运行截图 ====

![image-20240925160627955](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240925160627955.png)



## 2. 学习总结和收获

====

熟悉了python的语法。学到了很多编程知识。每日选作基本上都在做。





