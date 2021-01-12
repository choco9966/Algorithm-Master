import sys

def getSubsum(data) :
    '''
    n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합을 반환하는 함수를 작성하세요.
    '''

    '''
    완전 탐색 방법으로 할 것이다.
    
    start : 시작점
    end : 끝점
    '''
    
    result = -987987987987987
    
    for start in range(0, len(data)) :
        for end in range(start, len(data)) :
            # (start, end)
            
            mySum = 0
            
            for i in range(start, end+1) :
                mySum += data[i]
                
            result = max(result, mySum)
    
    # result
    
    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(getSubsum(data))

if __name__ == "__main__":
    main()
