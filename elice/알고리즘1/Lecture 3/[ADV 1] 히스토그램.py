import sys

def getRect(heights) :
    '''
    n개의 판자의 높이가 주어질 때, 이를 적당히 잘라 얻을 수 있는 직사각형의 최대 넓이를 반환하는 함수를 작성하세요.
    '''

    n = len(heights)

    if n <= 1 :
        return heights[0]

    mid = n//2

    left = getRect(heights[:mid])
    right = getRect(heights[mid:])

    leftPtr = mid-1
    rightPtr = mid

    curHeight = min(heights[leftPtr], heights[rightPtr])
    result = curHeight * (rightPtr - leftPtr + 1)

    while leftPtr-1 >= 0 or rightPtr+1 < n :
        leftHeight = heights[leftPtr-1] if leftPtr-1 >= 0 else -987987987987987
        rightHeight = heights[rightPtr+1] if rightPtr+1 < n else -987987987987987
        maxHeight = max(leftHeight, rightHeight)

        if leftHeight >= rightHeight :
            leftPtr -= 1
        else :
            rightPtr += 1

        curHeight = min(curHeight, maxHeight)
        result = max(result, curHeight * (rightPtr - leftPtr + 1))

    return max([result, left, right])

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(getRect(data))

if __name__ == "__main__":
    main()
