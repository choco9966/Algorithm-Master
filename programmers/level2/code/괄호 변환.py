def check_balanced(p):
    stack = []
    for i in list(p):
        if i == '(':
            stack.append('(')
        else:
            try:
                stack.pop()
            except:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

def split_balanced(p):
    cnt = 0
    for idx in range(len(p)):
        if p[idx] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return (idx+1)

    return idx + 1

def solution(p):
    answer = ''

    # 빈문자열인 경우 ''를 반환  
    if (p == '') | (check_balanced(p) == True): return p

    # 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
    idx = split_balanced(p)
    u, v = p[:idx], p[idx:]

    # 문자열 u가 올바른 괄호 문자열이라면 v에 대해 1을 수행
    if check_balanced(u) :
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        u = u[1:-1].replace('(', 'a')
        u = u.replace(')', 'b')
        u = u.replace('a', ')')
        u = u.replace('b', '(')
        answer = answer + u
    return answer
