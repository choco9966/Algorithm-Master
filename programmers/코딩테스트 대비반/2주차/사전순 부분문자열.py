def solution(s):
    stack = []
    
    for chr in s:
        while len(stack) > 0 and stack[-1] < chr:
            stack.pop()
        stack.append(chr)
    return "".join(stack)
