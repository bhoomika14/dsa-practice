"""
You will be given a list of 32 bit unsigned integers. 
Flip all the bits and return the result as an unsigned integer.

"""
from ctypes import c_uint8 as unsigned_byte
def flippingBits(n):
    return unsigned_byte(~n).value

n = 9
print(flippingBits(n))
print(~9)
print((1 << 32)-10) # convert to unsigned-32 bit representation
