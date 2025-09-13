"""
Given an integer array of N elements. 

You need to find the maximum sum of two elements such that sum is closest to zero.
"""
#Time complexity - O(NlogN), Space complexity - O(1)
def sum_closest_0(arr):
    arr.sort()
    n = len(arr)
    return arr[n-1]+arr[n-2]

arr = [-21, -67, -37, -18, 4, -65]
print(sum_closest_0(arr))
