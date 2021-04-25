import sys

def inversionCountInternal(data, start, end) :
    '''
    data[start] ~ data[end] 까지의 inversion 개수를 반환하고, 동시에 data[start] ~ data[end]를 정렬하는 함수
    '''
    if end - start <= 0 :
        return 0

    mid = (start + end) // 2

    left = inversionCountInternal(data, start, mid)
    right = inversionCountInternal(data, mid+1, end)

    temp = []

    leftPtr = start
    rightPtr = mid+1

    result = 0
    rightCnt = 0
    carryCnt = 0
    carryNumber = 0

    while leftPtr <= mid or rightPtr <= end :
        leftValue = data[leftPtr] if leftPtr <= mid else 987987987987987
        rightValue = data[rightPtr] if rightPtr <= end else 987987987987987

        if leftValue < rightValue :
            if len(temp) >= 1 and temp[-1] < leftValue :
                rightCnt += carryCnt
                carryCnt = 0

            result += rightCnt
            leftPtr += 1
            temp.append(leftValue)
        else :
            if len(temp) >= 1 and temp[-1] < rightValue :
                rightCnt += carryCnt
                carryCnt = 1
            else :
                carryCnt += 1

            rightPtr += 1
            temp.append(rightValue)

    for i in range(start, end+1) :
        data[i] = temp[i-start]

    return left + right + result

def inversionCount(data) :
    '''
    n개의 숫자가 list로 주어질 때, inversion 관계에 있는 숫자 쌍의 개수를 반환하는 함수를 작성하세요.
    '''

    dataPrime = list(data)
    return inversionCountInternal(dataPrime, 0, len(data)-1)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(inversionCount(data))

if __name__ == "__main__":
    main()
