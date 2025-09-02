"""
In the given array, each element appears an even number of times except one element which appears odd no. of times. 

Your task is to find the element which occurs an odd number of times.

"""
def find_odd_occurrence(nums):
    xor = 0
    for i in nums:
        xor^=i
    return xor

print(find_odd_occurrence([5,5,6,4,6]))
