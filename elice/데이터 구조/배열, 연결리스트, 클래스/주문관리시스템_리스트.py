class orderManager :
    '''
    주문을 처리하는 class를 작성합니다.
    '''

    def __init__(self) :
        '''
        이 부분은 고치지 마세요.
        '''
        self.data = []

    def addOrder(self, orderId) :
        '''
        주문번호 orderId를 추가합니다.
        '''
        self.data.append(orderId)

    def removeOrder(self, orderId) :
        '''
        주문번호 orderId를 제거합니다.
        '''
        self.data.remove(orderId)

    def getOrder(self, orderId) :
        '''
        주문번호 orderId가 몇 번째로 처리될지를 반환합니다.

        만약 주문번호 orderId가 존재하지 않으면 -1을 반환합니다. 
        '''
        if orderId not in self.data: 
            return -1 
        else: 
            return self.data.index(orderId) + 1
            

def main():
    manager = orderManager()

    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    manager.addOrder(2)
    manager.removeOrder(2)
    manager.addOrder(1818)
    manager.addOrder(8282)
    manager.addOrder(2255)
    manager.addOrder(6515)
    manager.removeOrder(1818)
    manager.addOrder(486)

    print(manager.getOrder(486))
    print(manager.getOrder(3))

    manager.addOrder(4860)

if __name__ == "__main__":
    main()
