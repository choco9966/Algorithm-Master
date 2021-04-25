import sys

def getDistPoints(a, b) :
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

def getDistBigInternal(points, start, end) :
    if end - start <= 0 :
        return 987987987987987

    mid = (start + end) // 2
    midX = (points[mid][0] + points[mid+1][0]) / 2

    leftDist = getDistBigInternal(points, start, mid)
    rightDist = getDistBigInternal(points, mid+1, end)

    minDistValue = min(leftDist, rightDist)
    temp = []
    tempConsider = []

    leftPtr = start
    rightPtr = mid+1

    while leftPtr <= mid or rightPtr <= end :
        leftYval = points[leftPtr][1] if leftPtr <= mid else 987987987987987
        rightYval = points[rightPtr][1] if rightPtr <= end else 987987987987987

        if leftYval <= rightYval :
            temp.append(points[leftPtr])
            leftPtr += 1
        else :
            temp.append(points[rightPtr])
            rightPtr += 1

        if temp[-1][0] >= midX - minDistValue and temp[-1][0] <= midX + minDistValue :
            tempConsider.append(temp[-1])

    for i in range(start, end+1) :
        points[i] = temp[i-start]

    considerN = len(tempConsider)

    result = 987987987987987

    for i in range(considerN) :
        for j in range(1, 13) :
            if i + j < considerN :
                result = min(result, getDistPoints(tempConsider[i], tempConsider[i+j]))

    return min(minDistValue, result)


def getDistBig(points) :
    '''
    n개의 점이 주어질 때, 가장 가까운 두 점 사이의 거리의 제곱을 반환하는 함수를 작성하세요.

    예를 들어, 점이 4개가 있고, 각각의 좌표가 (0, 3), (1, 1), (2, 2), (7, 1) 이라면 points에는 다음과 같이 그 정보가 저장됩니다.

    points = [ (0, 3), (1, 1), (2, 2), (7, 1) ]

    이 때, 가장 가까운 두 점 사이의 거리의 제곱은 2입니다.
    '''

    pointsPrime = list(points)
    pointsPrime.sort()

    return getDistBigInternal(pointsPrime, 0, len(points)-1)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    points = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        points.append( (line[0], line[1]) )

    print(getDistBig(points))

if __name__ == "__main__":
    main()
