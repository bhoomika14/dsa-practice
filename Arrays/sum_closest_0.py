"""
Given an integer array of N elements. 

You need to find the maximum sum of two elements such that sum is closest to zero.
"""
# Brute force - O(N^2)
def closestToZero(arr):
    closest = arr[0]+arr[1]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i]+arr[j])<abs(closest):
                closest = arr[i]+arr[j]
    
    return closest

       
arr = [-32, -12, -6, 13, 29]
print(closestToZero(arr))

# Two pointer approach - O(NLogN)
def closestSum(arr):
    arr.sort()
    l = 0
    r = len(arr)-1
    closest = arr[l]+arr[r]
    while l<r:
        if abs(arr[l]+arr[r])<abs(closest):
            closest=arr[l]+arr[r]

        if arr[l]+arr[r]>0:
            r-=1
        else:
            l+=1
        
    return closest

arr = [-32, -12, -6, 13, 29]
print(closestSum(arr))