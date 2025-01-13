words=list(input().split())
a={'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14,
   'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80,
   'ninety':90, 'hundred':100, 'thousand':1000, 'million':1000000,'negative':-1}
s=0
current=0
if words[0]=='negative':
    for i in range(1,len(words)):
        if words[i]=='million':
            s+=current*(1000000)
            current=0
        elif words[i]=='thousand':
            s+=current*(1000)
            current=0
        elif words[i]=='hundred':
            current=current*(100)
        else:
            current+=a[words[i]]
    s+=current
    s=s*(-1)
else:
    for i in range(len(words)):
        if words[i] == 'million':
            s += current * (1000000)
            current = 0
        elif words[i] == 'thousand':
            s += current * (1000)
            current = 0
        elif words[i] == 'hundred':
            current= current * (100)
        else:
            current += a[words[i]]
    s += current
print(s)