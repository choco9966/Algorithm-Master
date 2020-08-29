def solution(arrangement):
    answer = 0
    # 여는 괄호가 나오면, 닫힌 괄호가 나오기전까지 몇개의 레이저가 있는 지 확인해야 함 
    # 주의 : ()는 레이저이기때문에 하나의 문자열로 인식해야 함 
    arrangement = arrangement.replace('()', '-')
    stack = []
    for i in arrangement:
        if i == '(':
            stack.append(0)
        elif i == ')':
            stack.pop()  
            answer += 1
        else:
            answer += len(stack)
    return answer
