"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

"""
def rotated_array(nums, k):
    for i in range(k):
        value = nums[len(nums)-1]
        print(value)
        j=len(nums)-1
        while j>0:
            nums[j]=nums[j-1]
            j-=1
        nums[j]=value
    return nums

nums = [1,2,3,4,5,6,7]
k = 3
print(rotated_array(nums, k))
