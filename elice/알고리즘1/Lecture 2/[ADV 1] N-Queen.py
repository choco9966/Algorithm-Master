import sys
import itertools

def isPossible(assignment, n) :
    diagonalCheck1 = [ 0 for i in range(n+n) ]
    diagonalCheck2 = [ 0 for i in range(n+n) ]

    for i in range(n) :
        diagonalCheck1[(assignment[i] - i) + n] += 1
        diagonalCheck2[(assignment[i] + i) - n] += 1

    for i in range(n+n) :
        if diagonalCheck1[i] >= 2 or diagonalCheck2[i] >= 2 :
            return False

    return True

def nQueen(n) :
    '''
    n개의 Queen을 배치하는 경우의 수를 반환하는 함수를 작성하세요.
    '''

    myList = [ i for i in range(n) ]
    myPermutation = itertools.permutations(myList)
    cnt = 0

    for assignment in myPermutation :
        if isPossible(assignment, n) == True :
            cnt += 1

    return cnt

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    print(nQueen(n))

if __name__ == "__main__":
    main()