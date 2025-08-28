"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

"""
# TC - O(NlogN + N) => O(NlogN)
def missing_number(nums):
    nums.sort() # O(NlogN)
    for i in range(len(nums)+1):
        if i!=nums[i]:
            return i


# Approach 2: TC - O(N)
def find_missing_number(nums):
    XorNum = 0
    for i in range(1, len(nums)+1):
        XorNum^=i
        
    for i in nums:
        XorNum^=i

    return XorNum


nums = [0,1]
print(f"Missing number is {find_missing_number(nums)}")