"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 

You may assume that the majority element always exists in the array.
"""
# Approach 1 with TC - O(N) and SC - O(N)
def find_majority(nums):
    majority = len(nums)//2
    hashMap = {}
    for i in nums:
        if i in hashMap:
            hashMap[i] += 1
        else:
            hashMap[i] = 1

    for k, v in hashMap.items():
        if v>majority:
            return k



nums = [3,2,3]
print(find_majority(nums))