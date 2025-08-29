"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

"""
# Time complexit: O(N), Space complexity: O(N)
def duplicate_number(nums):
    d = dict()
    for i in nums:
        if i in d:
            return i
        d[i] = 1

# Time complexity: O(N), Space complexity: O(1)
def find_duplicate(nums):
    xor = 0
    for i in range(len(nums)):
        xor^= i^nums[i]
    return xor

nums = [3,1,3,4,2]
print(find_duplicate(nums))