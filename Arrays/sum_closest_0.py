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
