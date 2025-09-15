"""
You are given an integer array arr of size n+2. 

All elements of the array are in the range from 1 to n. 

Also, all elements occur once except two numbers which occur twice. Find the two repeating numbers.
"""
# Brute force - Time complexit - O(N), Space complexity - O(N)
def two_elements(n, arr):
    hashMap = {}
    result = []
    for i in arr:
        #if key is not in map/dictionary
        if i not in hashMap:
            hashMap[i]=i
        else:
            result.append(i)
    return result

# Indexing approach; Time complexity - O(N), Space Complexity - O(1)
def two_repeated(n, arr):
    result = []
    for i in range(len(arr)):
        index = abs(arr[i])
        if arr[index]>0:
            arr[index]=-arr[index]
        else:
            result.append(index)
    return result

n = 4
arr = [1, 2, 1, 3, 4, 3]
print(two_repeated(n, arr))