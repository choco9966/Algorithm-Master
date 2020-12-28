def findOrder(p) :
    '''
    괄호 p가 주어질 때, 각 괄호가 몇 번째로 계산되어야 하는 괄호인지를 list로 반환합니다.

    예를 들어, p='(()())' 일 경우, [3, 1, 1, 2, 2, 3] 을 반환합니다.
    '''

    result = [0] * len(p)
    stack = []
    cnt = 1
    
    for i in range(len(p)) :
        if p[i] == '(' :
            stack.append(i)
        else :
            result[i] = cnt
            result[stack.pop()] = cnt
            cnt += 1

    return result

def main():
    '''
    Do not change this code
    '''

    p = input()
    print(*findOrder(p))

if __name__ == "__main__":
    main()

