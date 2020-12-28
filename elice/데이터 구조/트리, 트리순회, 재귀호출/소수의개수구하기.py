import math 
def countPrimes(t):
    '''
    내 풀이 
    1부터 t까지의 수 중에서 소수의 개수를 반환합니다.
    속도가 굉장히 오래걸리는 문제점이 있음 
    모든 값에 대해서 소수인지 아닌지를 탐색하는 코드 
    '''
    cnt = 0
    for i in range(2, t+1): 
        flag = True 
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0: 
                flag = False
                break
        if flag == True: 
            cnt += 1 
    return cnt 

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    t = int(input())

    print(countPrimes(t))

if __name__ == "__main__":
    main()

import math
def countPrimes(t):
    '''
    강사님 풀이 
    1부터 t까지의 수 중에서 소수의 개수를 반환합니다.
    이중 for문을 사용하는게 아니라, 모든 소수의 여부를 담을 리스트를 먼저 생성
    소수가 판명된 값에 대해서 가능한 곱의 경우는 모두 소수가 아니다로 판정 ([0] 삽입) 
    예) 2가 소수 -> 4, 6, 8, 10, ... , 모두 [0] 삽입 
    예) 3이 소수 -> 3, 6, 9, 12, ... , 
    예) 4는 소수가 아님 (0) -> if s[i]에서 걸려서 패스 
    '''
    cnt = 0
    s = [0, 0] + [1] * (t - 1)
    for i in range(2, int(math.sqrt(t))+1):
        if s[i]:
            s[i*2::i] = [0] * ((t - i)//i)
    # 1인 값에 대해서 sum을 취함 
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
