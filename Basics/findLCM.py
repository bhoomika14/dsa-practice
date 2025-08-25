"""
Given an array of elements find its LCM
"""
def findLCM(arr):
    def findGCD(a, b):
        if a%b == 0:
            return b
        return findGCD(b, a%b)
    
    lcm = (arr[0]*arr[1]) // findGCD(arr[0], arr[1])
    for i in range(1, len(arr)):
        lcm *= arr[i] // findGCD(lcm, arr[i])

    return lcm

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"LCM of array {arr} is {findLCM(arr)}")
