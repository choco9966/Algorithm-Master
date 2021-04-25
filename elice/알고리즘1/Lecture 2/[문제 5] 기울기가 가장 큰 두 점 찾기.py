import sys

def getSlope(a, b) :
    return abs((a[1] - b[1]) / (a[0] - b[0]))

def maxSlope(points) :
    '''
    n개의 점들 중에서 2개의 점을 선택했을 때, 얻을 수 있는 기울기의 절댓값 중에서 가장 큰 값을 반환하는 함수를 작성하세요.
    '''

    result = -1
    n = len(points) 

    for i in range(n) :
        for j in range(i+1, n) :
            result = max(result, getSlope(points[i], points[j]))

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    points = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        points.append( (line[0], line[1]) )

    print("%.3lf" % maxSlope(points))

if __name__ == "__main__":
    main()
