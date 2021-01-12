import sys

def coinChange(n) :
    '''
    n원을 돌려주기 위해 필요한 동전 개수의 최솟값을 반환하는 함수를 작성하세요.
    '''

    coins = [100, 50, 10, 5, 1]
    result = 0

    for c in coins :
        numCoin = n // c
        result += numCoin
        n -= (numCoin * c)

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    print(coinChange(n))

if __name__ == "__main__":
    main()
