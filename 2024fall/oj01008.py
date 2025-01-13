import re
n=int(input())
answer=[]
Haab_months=['pop','no','zip','zotz','tzec','xul','yoxkin','mol','chen','yax','zac','ceh','mac','kankin','muan','pax','koyab','cumhu','uayet']
Tzolkin_days=['imix','ik','akbal','kan','chicchan','cimi','manik','lamat','muluk','ok','chuen','eb','ben','ix','mem','cib','caban','eznab','canac','ahau']
for i in range(n):
    Haab=input()
    Haab_day,Haab_year=re.findall(r'\d+',Haab)
    Haab_month=re.findall(r'[a-z]+',Haab)[0]
    month_th=Haab_months.index(Haab_month)
    if month_th<18:
        d=int(Haab_year)*365+month_th*20+int(Haab_day)
    else:
        d=int(Haab_year)*365+360+int(Haab_day)
    Tzolkin_year=d//260
    d1=d%260
    Tzolkin_day1=(d1)%13+1
    Tzolkin_day2=Tzolkin_days[(d1)%20]
    answer.append(f'{Tzolkin_day1} {Tzolkin_day2} {Tzolkin_year}')
print(n)
for a in answer:
    print(a)