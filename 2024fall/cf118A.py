word=input()
word=word.lower()
i=0
for i in range(len(word)):
    if word[i]!='a' and word[i]!='e' and word[i]!='i' and word[i]!='o' and word[i]!='u' and word[i]!='y':
        print('.'f"{word[i]}",end='')