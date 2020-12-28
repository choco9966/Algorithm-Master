def getMax2(n, myMatrix):
    '''
    크기 n x n 의 행렬 myMatrix내의 원소의 합, 최댓값, 두 번째 최댓값을 반환하는 함수.

    만약 myMatrix = [[1, 2, 3], [2, 3, 4], [3, 3, 4]]라면 (25, 4, 3) 을 반환한다.
    '''

    mySum = 0
    myMax = 0
    myMax2 = 0
    
    for matrix in myMatrix :
        for num in matrix :
            mySum += num
            if myMax2 < num :
                if myMax < num :
                    myMax2,myMax = myMax,num
                elif myMax > num :
                    myMax2 = num

    return (mySum, myMax, myMax2)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    myMatrix = []

    for i in range(n):
        myMatrix.append([int(v) for v in input().split()])

    print(getMax2(n, myMatrix))

if __name__ == "__main__":
    main()
