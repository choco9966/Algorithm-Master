class maxMachine :
    def __init__(self) :
        self.machine = []
        
    def addNumber(self, n) :
        self.machine.append(n)

    def removeNumber(self, n) :
        self.machine.remove(n)

    def getMax(self) :
        return max(self.machine)

def main():
    
    # myMachine이라는 instance를 생성 
    myMachine = maxMachine()

    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    myMachine.addNumber(1)
    myMachine.addNumber(2)
    myMachine.addNumber(3)
    myMachine.addNumber(2)

    print(myMachine.getMax())

    myMachine.removeNumber(3)

    print(myMachine.getMax())

    myMachine.removeNumber(2)

    print(myMachine.getMax())

    myMachine.removeNumber(2)

    print(myMachine.getMax())

if __name__ == "__main__":
    main()
