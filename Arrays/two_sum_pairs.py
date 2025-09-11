"""
Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

"""
# Brute force
def two_sum(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == 0:
                result.append([arr[i], arr[j]])
        
    return result
arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
print(two_sum(arr))