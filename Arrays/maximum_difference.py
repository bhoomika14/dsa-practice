"""
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), 

such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1

"""
# Brute force - Time complexity - O(N^2)
def maximum_difference(nums):
    maximum = -1
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j]-nums[i] > 0 and nums[j]-nums[i] > maximum:
                maximum = nums[j]-nums[i]

    return maximum

# Time complexity - O(N)
def max_difference(nums):
    maximum = -1
    minimum = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > minimum:
            maximum = max(maximum, nums[i]-minimum)
        else:
            minimum = nums[i]
    return maximum

nums = [1, 5, 2, 10]
print(max_difference(nums))