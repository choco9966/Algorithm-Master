LIMIT_NUMBER = 1000000007

def getPower(m, n):
    '''
    m^n 을 LIMIT_NUMBER로 나눈 나머지를 반환하는 함수를 작성하세요.
    '''
    if n == 0 :
        return 1
    temp = getPower(m,n//2)
    if n % 2 :
        return temp * temp * m % 1000000007
    else :
        return temp * temp % 1000000007

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    myList = [int(v) for v in input().split()]

    print(getPower(myList[0], myList[1]))

if __name__ == "__main__":
    main()
