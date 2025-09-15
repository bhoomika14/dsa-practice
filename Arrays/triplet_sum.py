"""
Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.

"""
# Brute force - Time complexity - O(N^3), Space complexity - O(1)
def triplet_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i):
            for k in range(j):
                if arr[i]+arr[j]+arr[k]==target:
                    return True
    return False

def triplets(arr, target):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(arr[i])
            print(arr[j])
            print(target-(arr[i]+arr[j]))
            if target-(arr[i]+arr[j]) in arr:
                return True
    return False
    
arr = [1, 4, 6, 8, 10, 45]
target = 13
print(triplets(arr, target))
