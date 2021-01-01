def solution(s):    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')
    myStack = []
    for i in s: 
        if i == "(": 
            myStack.append(i)
        else:
            try:
                myStack.pop()
            except:
                return False
    if len(myStack) == 0: 
        return True
    else:
        return False
