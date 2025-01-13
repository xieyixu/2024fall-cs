def merge_count_split(arr,temp,left,right):
    if left>=right:
        return 0
    mid=(left+right)//2
    inv_count=0
    inv_count+=merge_count_split(arr,temp,left,mid)
    inv_count+=merge_count_split(arr,temp,mid+1,right)  #分割开来，统计逆序数。
    inv_count+=merge_and_count(arr,temp,left,mid,right)  #合并两个有序数组后再统计逆序数。
    return inv_count
def merge_and_count(arr,temp,left,mid,right):
    i=left
    j=mid+1
    k=left
    inv_count=0
    while i<=mid and j<=right:
        if arr[i]<=arr[j]:
            temp[k]=arr[i]
            i+=1
        else:
            temp[k]=arr[j]
            j+=1
            inv_count+=(mid-i+1)
        k+=1
    while i<=mid:
        temp[k]=arr[i]
        i+=1
        k+=1
    while j<=right:
        temp[k]=arr[j]
        j+=1
        k+=1
    for _ in range(left,right+1):
        arr[_]=temp[_]
    return inv_count
def count_inversion(arr):
    n=len(arr)
    temp=[0]*n
    return merge_count_split(arr,temp,0,n-1)

n=int(input())
a=list(map(int,input().split()))
print(count_inversion(a))