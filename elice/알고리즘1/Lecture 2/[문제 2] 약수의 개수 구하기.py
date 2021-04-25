def numDivisor(n):
    '''
    n의 약수의 개수를 반환하는 함수를 작성하세요.
    '''
    cnt = 0
    for i in range(1,n+1) :
        cnt += (n % i == 0)

    return cnt

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    number = int(input())
    print(numDivisor(number))

if __name__ == "__main__":
    main()
