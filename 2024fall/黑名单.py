blacklist=[1,2,3,4,5,6,7,8,9,10]
sender_IP=20
def  check():
    for i in range(10):
        if sender_IP==blacklist[i]:
            print('no')
            return 0
    else:
        print(sender_IP)
    return 0
check()