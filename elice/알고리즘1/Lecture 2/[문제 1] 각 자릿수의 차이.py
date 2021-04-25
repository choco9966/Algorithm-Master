def diffDigit(a, b) :
    '''
    a, b의 서로 다른 자리수의 개수를 반환한다
    '''
    cnt = 0
    while a != 0 and b != 0 :
        cnt += a%10 != b%10
        a = a // 10
        b = b // 10
    if a == 0 :
        while b != 0 :
            cnt += 1
            b = b // 10
    else :
        while a != 0 :
            cnt += 1
            a = a // 10

    return cnt

def main():
    '''
    Do not change this code
    '''

    a = int(input())
    b = int(input())

    print(diffDigit(a, b))


if __name__ == "__main__":
    main()
