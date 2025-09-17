"""
Complete the theGreatXor function in the editor below. 

It should return an integer that represents the number of values satisfying the constraints.

Constraints - a^x > x and a < x
"""
#Brute force - Time complexity - O(N)
def theGreatXor(x):
    cnt=0
    for i in range(1,x):
        print(f"{i}- {i^x}")
        if i^x>x:
            cnt+=1
    return cnt

# Bit manipulation approach - O(logN)
def great_xor(x):
    binary = ""
    n = x
    while n>0:
        binary += str(n&1)
        n>>=1
    bit_length = len(binary)
    return (2**bit_length)-x

x = 100
print(great_xor(x))