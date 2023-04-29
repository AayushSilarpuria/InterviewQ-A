# GMWARE
# Question 4:

# Given a list of integers nums and an integer k, write a function to determine whether there exists a contiguous subarray of nums with a sum of k.

# For example,
# if nums is [1, 2, 3, 4] and k is 6, the function should return true, since the subarray [2, 3] has a sum of
# 6.
# If nums is [1, 2, 3, 4] and k is 9, the function should return false, since there is no contiguous

# subarray of nums with a sum of 9.

def has(nums, k):
    window_sum = 0
    left = 0
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum > k:
            window_sum -= nums[left]
            left += 1
        if window_sum == k:
            return True
    return False


num = [1, 2, 3, 4]
j = 6
print(has(num, j))
