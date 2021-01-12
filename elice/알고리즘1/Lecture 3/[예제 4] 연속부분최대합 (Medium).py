import sys
import math

def getSubsum(data) :
    '''
    n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합을 반환하는 함수를 작성하세요.
    '''

    if len(data) <= 1 :
        return data[0]
        
    n = len(data)
    mid = n // 2
    
    left = getSubsum(data[:mid]) # 0 ~ mid-1
    right = getSubsum(data[mid:]) # mid ~ n
    
    leftSum = 0
    rightSum = 0
    
    # 왼쪽
    
    Sum = 0
    
    for i in range(mid-1, -1, -1) :
        Sum += data[i]
        leftSum = max(Sum, leftSum)
        
    # 오른쪽
    
    Sum = 0
    
    for i in range(mid, n) :
        Sum += data[i]
        rightSum = max(Sum, rightSum)
        
    return max([left, right, leftSum + rightSum])

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(getSubsum(data))

if __name__ == "__main__":
    main()

	