# 쉬운 코드 
def solution(brown ,red):
    width, height = 0, 0
    total = brown + red

    for height in range(1, total):
        width = total // height
        print(width, height)
        if (width-2) * (height-2) == red:
            return [width, height]

# 빠른 코드 (위의 경우 대비 약 10배이상 빠름) 
# 약수에 대한 경우의 수 계산하기 
import math 
def getDivisor(n):
    '''
    숫자 n이 주어지면 n의 약수를 모두 구하는 함수
        
    만약 n = 12이면, result = [1, 2, 3, 4, 6, 12]를 반환한다.
    '''
    sol = []
    result = []
    for i in range(1, int(math.sqrt(n)) + 1): 
        if n % i == 0: 
            result.append(i)
    
    temp = sorted([n//x for x in result if not n//x in result])
    return temp + result

def solution(brown, red):
    n = brown + red 
    total = getDivisor(n)
    for i in total: 
        if (i >= n//i) and ((i-2) * (n//i - 2) == red) : 
            return [i, n//i]
