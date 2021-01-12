import sys
import math

def mergeSort(data) :
    '''
    n개의 숫자를 합병정렬을 이용하여 정렬한 결과를 list로 반환하는 함수를 작성하세요.
    '''

    if len(data) <= 1 :
        return data
        
    mid = len(data) // 2
    
    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])
    
    result = []
    
    leftPtr = 0
    rightPtr = 0
    
    while leftPtr < len(left) or rightPtr < len(right) :
        leftValue = left[leftPtr] if leftPtr < len(left) else math.inf
        rightValue = right[rightPtr] if rightPtr < len(right) else math.inf
        
        if leftValue < rightValue :
            leftPtr += 1
            result.append(leftValue)
        else :
            rightPtr += 1
            result.append(rightValue)
        

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(*mergeSort(data))

if __name__ == "__main__":
    main()
