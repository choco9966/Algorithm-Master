def checkParen(p):
    '''
    괄호 문자열 p의 쌍이 맞으면 "YES", 아니면  "NO"를 반환
    '''

    '''
    0. 기저조건 처리
    1. p에서 인접한 괄호 '()' 를 찾는다
    2. 이 친구를 제거한다
    3. checkParen 에게 다시 물어본다
    '''
    
    if len(p) <= 1 :
        if len(p) == 0 :
            return "YES"
        else : # '(' ')'
            return "NO"
    elif p == "()" :
        return "YES"
        
    for i in range(len(p)-1) :
        if p[i] == '(' and p[i+1] == ')' :
            q = p[:i]  + p[i+2:]
            
            return checkParen(q)
    
    return "NO"

def main():
    '''
    Do not change this code
    '''

    x = input()
    print(checkParen(x))

if __name__ == "__main__":
    main()




