import re
n=int(input())
m=[input() for _ in range(n)]
alphabet = {26:'Z',0:'Z',1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L',
            13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X',
            25: 'Y'}
for s in m:
    if re.search(r'^R\d+C\d+$',s):
        r,c=re.findall(r'\d+',s)
        column=[]
        c=int(c)
        while c>0:
            if c%26==0:
                s=c%26
                column.append(alphabet[s])
                c//=26
                c-=1
            else:
                s = c % 26
                column.append(alphabet[s])
                c //= 26
        column.reverse()
        print(f'{"".join(s for s in column)}{r}')
    else:
        l,n=re.findall(r'[A-Z]',s),re.findall(r'\d+',s)
        column=0
        for i in range(len(l)):
            find=l[i]
            first=next((key for key ,value in alphabet.items() if value==find),None)
            column+=26**(len(l)-i-1)*first
        print(f'R{"".join(s for s in n)}C{column}')