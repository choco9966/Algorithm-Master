import sys

def numSubstr(A, B) :
    '''
    B가 A에 포함되어 있는 횟수를 반환하는 함수를 작성하세요.
    '''
    cnt = 0
    for i in range(len(A)-len(B)+1) :
        cnt += (B == A[i:i+len(B)])

    return cnt

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    A = input()
    B = input()

    print(numSubstr(A, B))

if __name__ == "__main__":
    main()
