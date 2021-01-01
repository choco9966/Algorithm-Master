def solution(s):
    stack = []
    PAIRS = {"(": ")", "[": "]", "{": "}"}
    
    for chr in s:
        if len(stack) == 0 and chr not in PAIRS:
            return False
            break
        elif chr in PAIRS:
            stack.append(chr)
        elif chr == PAIRS[stack[-1]]:
            stack.pop()
        else:
            return False
            break
                
    return len(stack) == 0
