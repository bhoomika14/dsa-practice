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

# Approach 2
def two_sum_pairs(arr):
    arr.sort() # O(NlogN)
    l = 0
    r = len(arr)-1
    result = []
    while(l<r):
        if arr[l]+arr[r]==0:
            result.append([arr[l], arr[r]])
            l+=1
        elif arr[l]+arr[r] < 0:
            l+=1
        else:
            r-=1
        
    return result


# Time complexity - O(N)
def two_sum_pairs_hashing(arr):
    hashMap = {}
    result = []
    for i in arr:
        if 0-i not in hashMap:  # O(1)
            hashMap[i] = 1
        else:
            result.append([i, 0-i])
    return result

arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
print(two_sum_pairs_hashing(arr))

