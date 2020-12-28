import sys
sys.setrecursionlimit(1000001)

LIMIT_NUMBER = 1000000007
def matrix_multifly(a, b) :
    n = len(a)
    result = [[0 for i in range(n)] for i in range(n)]
    for i in range(n) :
        for j in range(n) :
            for k in range(n) :
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= LIMIT_NUMBER
    return result
def squaring_mat(mat, m):
    '''
    행렬 mat의 m제곱을 반환하는 함수를 작성합니다.
    '''
    
    if m == 1 :
        return mat
    temp = squaring_mat(mat,m//2)
    if m % 2 :
        return matrix_multifly(matrix_multifly(temp, temp),mat)
    else :
        return matrix_multifly(temp, temp)


def get_input():
    '''
    이 부분은 수정하지 마세요.
    '''

    n, m = [int(x) for x in input().strip().split(' ')]

    matrix = []
    for i in range(n):
        row = [int(x) for x in input().strip().split(' ')]
        matrix.append(row)

    return matrix, m

def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    matrix, m = get_input()

    result = squaring_mat(matrix, m)

    for line in result :
        print(*line)

if __name__ == '__main__':
    main()
