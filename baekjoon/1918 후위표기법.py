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

# 우선순위를 넣어서 코드를 좀 더 간결하게 하는 방법 
prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2, 
    '(': 1
}

mess = str(input())
result = ''
stack = []
for m in mess: 
    if m.isalpha() or m.isdecimal(): # m의 알파벳인지 여부 확인 
        result += m # 알파벳(숫자)는 바로 출력 
    else: 
        if m == '(': 
            stack += '('
        elif m == ')': # ')'가 입력으로 들어온 경우  
            while stack and stack[-1] != '(': # '(' 나올때까지 계속 출력 
                result += stack.pop() 
            stack.pop() # '(' 출력 
        else: 
            # 다른 사칙연산이 나오기전까지 제거 / 자기보다 우선순위가 높은 연산자는 모두 출력 
            while stack and (prec[m] <= prec[stack[-1]]): 
                result += stack.pop()
            stack += m
while stack: 
    result += stack.pop() 
print(result)
