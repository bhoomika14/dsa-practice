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
        
        if hashMap[i]>majority:
            return i


# Approach 2: Moore Voting Algorithm - TC is O(N) and SC is O(1)
def find_majority_element(nums):
    candidate = 0 
    count = 0
    for i in range(len(nums)):
        if count == 0:
            candidate = nums[i]
            count = 1
        else:
            if candidate == nums[i]:
                count+=1
            else:
                count-=1
    return candidate

nums = [5, 5, 1, 5, 2, 5, 3, 5, 4, 5, 6, 5, 7]
print(find_majority_element(nums))