import math
def getAnswer(n):
    '''
    마지막에 켜져 있는 컴퓨터의 대수를 반환하는 함수입니다.
    '''
    
    return int(math.sqrt(n))


def main():
    '''
        이 부분은 수정하지 마세요.
        '''
    print(getAnswer(int(input())))

if __name__ == "__main__":
    main()
