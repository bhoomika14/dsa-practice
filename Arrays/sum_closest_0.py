"""
Given an integer array of N elements. 

You need to find the maximum sum of two elements such that sum is closest to zero.
"""
#Time complexity - O(NlogN), Space complexity - O(1)
def sum_closest_0(arr):
    arr.sort()
    print(arr)
    l = 0
    r = len(arr)-1
    while l<r:
        minimum = arr[l]+arr[r]
        if minimum > 0:
            r-=1
        elif minimum < 0:
            l+=1
        else:
            return minimum
    return minimum
       
arr = [5, -3, 7, -8, 10, -1]
print(sum_closest_0(arr))
