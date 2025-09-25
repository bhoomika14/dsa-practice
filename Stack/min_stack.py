"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

"""

# Time complexity - O(1), Space complexity - O(N)
def push(val):
    stack.append(val)
    if len(minimum)==0:
        minimum.append(val)

    elif val < minimum[-1]:
        minimum.append(val)
        
    else:
        minimum.append(minimum[-1])

def pop():
    stack.pop()
    minimum.pop()

def top():
    if len(stack)!=0:
        return stack[-1]

def getMin():
    return minimum[-1]
    
stack = []
minimum = []
print(push(-2))
print(push(0))
print(push(-3))
print(getMin())
print(pop())
print(top())
print(getMin())

    

