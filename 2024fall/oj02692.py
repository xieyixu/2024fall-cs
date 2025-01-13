letter={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11}
letter_list=list(letter.keys())
def check(a,data_1,data_2,data_3):
    sum_1_left=sum(a[letter[s]] for s in data_1[0])
    sum_1_right=sum(a[letter[s]] for s in data_1[1])
    sum_2_left=sum(a[letter[s]] for s in data_2[0])
    sum_2_right=sum(a[letter[s]] for s in data_2[1])
    sum_3_left=sum(a[letter[s]] for s in data_3[0])
    sum_3_right=sum(a[letter[s]] for s in data_3[1])
    find_1=False
    find_2=False
    find_3=False
    if (sum_1_left==sum_1_right and data_1[2]=='even') or (sum_1_left>sum_1_right and data_1[2]=='up') or (sum_1_left<sum_1_right and data_1[2]=='down'):
        find_1=True
    if (sum_2_left==sum_2_right and data_2[2]=='even') or (sum_2_left>sum_2_right and data_2[2]=='up') or (sum_2_left<sum_2_right and data_2[2]=='down'):
        find_2=True
    if (sum_3_left==sum_3_right and data_3[2]=='even') or (sum_3_left>sum_3_right and data_3[2]=='up') or (sum_3_left<sum_3_right and data_3[2]=='down'):
        find_3=True
    return find_1 and find_2 and find_3

n=int(input())
for _ in range(n):
    input_1=input().split()
    input_2=input().split()
    input_3=input().split()
    a=[0]*12
    for i in range(12):
        a[i]=1
        if check(a,input_1,input_2,input_3):
            print(f'{letter_list[i]} is the counterfeit coin and it is heavy.')
            break
        a[i]=-1
        if check(a,input_1,input_2,input_3):
            print(f'{letter_list[i]} is the counterfeit coin and it is light.')
            break
        a[i]=0