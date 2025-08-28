"""
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.

Write an algorithm with O(log n) runtime complexity.
"""

def binary_search(arr, target):
    l = 0
    r = len(arr)-1
    while(l<=r):
        mid = (l+r)//2
        if target > arr[mid]:
            l = mid+1
        elif target < arr[mid]:
            r = mid-1
        else:
            if target == arr[mid]:
                return mid
    return -1      

nums = [-1,0,3,5,9,12]
target = 5
print(f"Target {target} found at index {binary_search(nums, target)}")