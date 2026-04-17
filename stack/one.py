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