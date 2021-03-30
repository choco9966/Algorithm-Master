# 참고자료 : https://jamanbbo.tistory.com/53
mess = str(input())
result = ''
stack = []
for m in mess: 
    if m.isalpha() or m.isdecimal(): # m의 알파벳인지, 숫자인지 여부 확인 
        result += m # 알파벳(숫자)는 바로 출력 
    else: 
        if m == '(': 
            stack += '('
        elif m == '*' or m == '/': 
            while stack and (stack[-1] == '*' or stack[-1] == '/'): 
                result += stack.pop() 
            stack += m
        elif m == '+' or m == '-': 
            # 다른 사칙연산이 나오기전까지 제거 
            while stack and (stack[-1] != '('): 
                result += stack.pop()
            stack += m
        else: # ')'가 입력으로 들어온 경우  
            while stack and stack[-1] != '(': # '(' 나올때까지 계속 출력 
                result += stack.pop() 
            stack.pop() # '(' 출력 

while stack: 
    result += stack.pop() 
print(result)
