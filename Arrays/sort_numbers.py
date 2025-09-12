"""
Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
Note: You need to solve this problem without utilizing the built-in sort function.

"""
# Time complexity = O(N), Space complexity = O(1)
def three_pointer_approach(arr):
    l = 0
    r = len(arr)-1
    m = len(arr)//2

    while l<m and r>m:
        while l<m and arr[l] == 0:
            l+=1
        
        if l<m:
            arr[l], arr[m] = arr[m], arr[l]
        
        while r>m and arr[r] == 2:
            r-=1

        if r>m:
            arr[r], arr[m] = arr[m], arr[r]
    
    return arr

arr = [0, 1, 2, 0, 1, 2]
print(three_pointer_approach(arr))