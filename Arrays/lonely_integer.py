"""
Given an array of integers, where all elements but one occur twice, find the unique element.
"""
def lonelyinteger(a):
    # Write your code here
    xor = 0
    for i in range(len(a)):
        xor^=a[i]
    return xor

a = [1,1,2]
print(lonelyinteger(a))