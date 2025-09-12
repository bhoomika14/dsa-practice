"""
Given an array arr consisting of only 0's and 1's in random order. 

Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.

"""
# Time complexity - O(N), Space complexity - O(1)
def segregate(arr):
    l = 0
    n = len(arr) - 1
    while l<n:
        if arr[l] >= arr[n]:
            arr[n], arr[l] = arr[l], arr[n]
            l+=1
        
    return arr

def two_pointer_approach(arr):
    l = 0
    r = len(arr)-1
    while l<r:
        while l<=r and arr[l]==0:
            l+=1

        while l<=r and arr[r]==1:
            r-=1
        
        if l<r:
            arr[r], arr[l] = arr[l], arr[r]
    
    return arr



    

arr = [0, 0, 0, 1, 0]
print(segregate(arr))
print(two_pointer_approach(arr))