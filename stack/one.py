# Q1 what is stack.
# stack = []

# stack.append(10)  # push
# stack.append(20)
# stack.append(30)

# print(stack.pop())  # pop → 30
# print(stack[-1])    # peek → 20

# 👉 Stack is a linear data structure that follows LIFO (Last In First Out) where insertion and deletion happen from one end called TOP.

# for reversing a string using stack
def reverse_string(s):
    stack = []
    
    # Push each character of the string onto the stack
    for char in s:
        stack.append(char)
    
    reversed_str = ''
    
    # Pop characters from the stack and build the reversed string
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str