"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

"""
def pairs(opening, closing):
    return (opening=="(" and closing==")") or (opening=="[" and closing=="]") or (opening=="{" and closing=="}")

stack = []
def isValid(s):
    for i in s:
        if len(stack)!=0 and pairs(stack[-1], i):
            stack.pop()
        else:
            stack.append(i)

    return True if len(stack)==0 else False


s="]"
print(isValid(s))
        

