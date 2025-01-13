height=list(map(int,input().split()))
n=len(height)
if n<3:
    print(0)
else:
    left,right=0,len(height)-1
    left_max,right_max=0,0
    count=0
    while left<right:
        if height[left]<height[right]:
            if height[left]>=left_max:
                left_max=height[left]
            else:
                count+=left_max-height[left]
            left+=1
        else:
            if height[right]>=right_max:
                right_max=height[right]
            else:
                count+=right_max-height[right]
            right-=1
    print(count)