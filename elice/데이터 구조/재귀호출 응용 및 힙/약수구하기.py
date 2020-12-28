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
    return result + temp

def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    print(getDivisor(int(input())))
          
if __name__ == "__main__":
    main()
