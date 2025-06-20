T = int(input())
nums = list(map(int, input().split()))
nums.sort()
left, right = 0, len(nums) - 1
closest_sum = None
min_diff = float('inf')

while left < right:
    current_sum = nums[left] + nums[right]
    current_diff = abs(current_sum - T)
    if current_diff < min_diff or (current_diff == min_diff and current_sum < closest_sum):
        min_diff = current_diff
        closest_sum = current_sum
    if current_sum < T:
        left += 1
    elif current_sum > T:
        right -= 1
    else:
        break
print(closest_sum)