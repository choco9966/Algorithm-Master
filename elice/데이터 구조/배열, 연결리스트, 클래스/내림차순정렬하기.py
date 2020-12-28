class maxMachine :
    def __init__(self) :
        self.machine = []

    def addNumber(self, n) :
        self.machine.append(n)

    def removeNumber(self, n) :
        self.machine.remove(n)

    def getMax(self) :
        return max(self.machine)

def sorting(myList) :
    '''
    myList를 내림차순으로 정렬하여 반환하는 함수를 작성하세요.

    예를 들어, myList = [5, 2, 3, 1] 이라면 [5, 3, 2, 1] 을 반환해야 합니다.

    단, maxMachine class를 이용하도록 합니다. 
    '''

    myMachine = maxMachine()
    for n in myList: 
        myMachine.addNumber(n)

    return sorted(myMachine.machine, reverse=True)

def main():
    '''
    이 곳은 수정하지 마세요.
    '''

    myList = [int(v) for v in input().split()]

    print(sorting(myList))

if __name__ == "__main__":
    main()
