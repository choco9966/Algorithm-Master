import math

def getDivisor(n):
    '''
    숫자 n이 주어지면 n의 약수를 모두 구하는 함수
        
    만약 n = 12이면, result = [1, 2, 3, 4, 6, 12]를 반환한다.
    '''
    result = []
    
    for x in range(1,int(math.sqrt(n))+1) :
        if n % x == 0 :
            result.append(x)
    temp = [n//x for x in result if not n//x in result]
    temp.reverse()
    result = result + temp

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    print(getDivisor(int(input())))
          
if __name__ == "__main__":
    main()
