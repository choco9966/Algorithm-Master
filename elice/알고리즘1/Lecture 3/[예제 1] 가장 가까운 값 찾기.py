import sys
import math

def getNearestInternal(data, m) :
    ‘’'
    n개의 숫자가 list로 주어지고, 숫자 m이 주어질 때,
    m보다 작거나 같은 숫자 중 최댓값,
    m보다 큰 숫자 중 최솟값을 반환하는 함수
    ‘’'
    
    if len(data) == 1 :
        if data[0] <= m :
            return (data[0], math.inf)
        else :
            return (-math.inf, data[0])
            
    elif len(data) == 2 :
        # [1, 3] 9
        if data[1] <= m :
            return (data[1], math.inf)
            
        # [1, 11] 9
        elif data[0] <= m and m < data[1] :
            return (data[0], data[1])
            
        # [10, 11] 9
        else :
            return (-math.inf, data[0])
        
    # [1, 3, 10, 11, 14, 18] 9
    
    mid = len(data) // 2
    
    if data[mid] <= m :
        return getNearestInternal(data[mid:], m)
    else :
        return getNearestInternal(data[:mid+1], m)

def getNearest(data, m) :
    ‘’'
    n개의 숫자가 list로 주어지고, 숫자 m이 주어질 때, n개의 숫자 중에서 m과 가장 가까운 숫자를 반환하는 함수를 작성하세요.
    ‘’'
    
    value = getNearestInternal(data, m)
    
    # value[0] <= m < value[1]

    if m - value[0] <= value[1] - m :
        return value[0]
    else : 
        return value[1]

def main():
    ‘’'
    이 부분은 수정하지 마세요.
    ‘’'

    data = [int(x) for x in input().split()]
    m = int(input())

    print(getNearest(data, m))

if __name__ == “__main__“:
    main()
