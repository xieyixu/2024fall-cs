def day(date,delta):
    n1=0
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        n = 0
        a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(month - 1):
            n += a[i]
        n = n + day
        n1 = n + delta
        return n1
    else:
        n = 0
        a = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(month - 1):
            n+=a[i]
        n=n+day
        n1=n+delta
        return n1

def year(date,delta):
    year = int(date[0:4])
    n=day(date,delta)
    while True:
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            if n>365:
                n=n-365
                year=year+1
            else:
                return n , year
        else:
            if n>366:
                n=n-366
                year=year+1
            else:
                return n,year


def month_and_day(n,year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        s=0
        i=0
        while s<n:
            s=s+a[i]
            i+=1
        day=n-s+a[i-1]
        return day,i
    else:
        a = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        s = 0
        i = 0
        while s < n:
            s = s + a[i]
            i += 1
        day = n - s+a[i-1]
        return day,i

date=input()
x=int(input())
y = int(date[0:4])
m = int(date[5:7])
d = int(date[8:10])
n1,y1=year(date,x)
d1,m1=month_and_day(n1,y1)
print(f"{y1}-{m1:02d}-{d1:02d}")


