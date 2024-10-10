n=int(input())
words=[]
for _ in range(n):
    word=input()
    words.append(word)
for word in words:
    if len(word)<=10:
        print(word)
    else:
        print(f"{word[0]}{len(word)-2}{word[-1]}")