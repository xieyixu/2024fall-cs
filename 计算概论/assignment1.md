# Assignment #1: 自主学习

Updated 0110 GMT+8 Sep 20, 2024

2024 fall, Complied by ==曾弘倓  物院  2400011513==





## 1. 题目

### 02733: 判断闰年

http://cs101.openjudge.cn/practice/02733/



思路：基于题目所给过程，直接写出程序。耗时可能大约1~2分钟。



##### 代码

```c++
#include<iostream>
using namespace std;
int main()
{
	int a;
	cin >> a;
	if ((a % 4 == 0 && a % 100 != 0) || (a % 400 == 0 && a % 3200 != 0))
	{
		cout << "Y" << endl;
	}
	else cout << "N" << endl;
	return 0;
}
```



代码运行截图 ====



![image-20240920104516902](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240920104516902.png)

### 02750: 鸡兔同笼

http://cs101.openjudge.cn/practice/02750/



思路：同上，也是基于题目所给过程直接写出程序。耗时也是大约1~2分钟。



##### 代码

```c++
#include<iostream>
using namespace std;
int main()
{
	int a, b, c;
	cin >> a;
	if (a % 4 == 0)
	{
		b = a / 2;
		c = a / 4;
		cout << c << " " << b << endl;
	}
	else if (a % 2 == 0)
	{
		b = a / 2;
		c = (a - 2) / 4 + 1;
		cout << c << " " << b << endl;
	}
	else
	{
		cout << 0 << " " << 0 << endl;
	}
	return 0;
}

```



代码运行截图 ====

![image-20240920104844370](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240920104844370.png)



### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：基于题目所给过程直接写出程序。耗时1分钟



##### 代码

```python
m,n=map(int,input().split())
s=m*n
print(int(s/2))
```



代码运行截图 ====

![image-20240920110321080](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240920110321080.png)



### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：铺上的地砖的总长要大于等于广场的长，总宽大于等于广场的宽。耗时大约3分钟。



##### 代码

```python
import math
n,m,a=map(int,input().split())
s=(math.ceil(n/a))*(math.ceil(m/a))
print(s)
```



代码运行截图 ====

![image-20240920110436933](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240920110436933.png)



### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：直接依据题目给出代码。耗时1分钟



##### 代码

```python
a1=input()
a2=input()
a1=a1.lower()
a2=a2.lower()
if a1<a2:
    print(-1)
elif a1>a2:
    print(1)
else:
    print(0)
```



代码运行截图 ====

![image-20240920111810326](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240920111810326.png)





### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：耗时大约3分钟



##### 代码

```python
a=int(input())
i=0
m=0
while i<a:
    p,v,n=map(int,input().split())
    i+=1
    if p+v+n>1:
        m=m+1

print(m)
```



代码运行截图 ====

![image-20240920110747434](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240920110747434.png)



## 2. 学习总结和收获

====

学习了python的基本编程语法，可以使用python编写较基础的程序。复习巩固了C++。

做了cs101计概（计算机基础1）中的一部分编程题目。





