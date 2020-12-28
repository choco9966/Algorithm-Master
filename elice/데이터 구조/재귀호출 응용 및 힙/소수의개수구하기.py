import math
def countPrimes(t):
    '''
    1부터 t까지의 수 중에서 소수의 개수를 반환합니다.
    '''
    cnt = 0
    s = [0, 0] + [1] * (t - 1)
    for i in range(2, int(math.sqrt(t))+1):
        if s[i]:
            s[i*2::i] = [0] * ((t - i)//i)
    for i in range(2,t+1) :
        cnt += s[i]
    return cnt


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    t = int(input())

    print(countPrimes(t))

if __name__ == "__main__":
    main()
