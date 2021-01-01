def solution(arrangement):
    answer = 0
    stack = []
    
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            stack.append('(')
            
        else:
            if arrangement[i-1] == '(':
                stack.pop()
                answer += len(stack)
            else:
                stack.pop()
                answer += 1
                
    return answer


from collections import deque
def solution(arrangement):
    answer = 0
    myStack = []
    arrangement = deque(arrangement)
    while arrangement: 
        ele = arrangement.popleft()
        # 레이저 
        if ele == '(' and arrangement[0] == ')': 
            answer += len(myStack) 
            arrangement.popleft() 
        # 막대인 경우 
        elif ele == '(' and arrangement[0] == '(': 
            myStack.append('(')
        # 막대가 끝나는 경우 
        else: 
            # 막대가 끝나는 부분에서 한개의 조각이 더 생김 
            answer += 1
            myStack.pop()
    return answer
