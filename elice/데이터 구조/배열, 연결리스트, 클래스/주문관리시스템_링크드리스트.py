class LinkedList: 
    def __init__(self): 
        self.key = None 
        self.value = None 
        
class orderManager :
    '''
    주문을 처리하는 class를 작성합니다.
    '''

    def __init__(self) :
        '''
        이 부분은 고치지 마세요.
        '''
        self.data = []
        self.start = None 
        self.end = None 

    def addOrder(self, orderId) :
        '''
        주문번호 orderId를 추가합니다.
        '''
        if self.start == None: 
            self.start = LinkedList()
            self.start.key = orderId 
            self.start.value = None 
            self.end = self.start 
        else:
            self.myNext = LinkedList()
            self.myNext.key = orderId
            self.myNext.value = None 
            self.end.value = self.myNext 
            self.end = self.myNext 

    def removeOrder(self, orderId) :
        '''
        주문번호 orderId를 제거합니다.
        '''
        # 주문번호를 찾아야함 
        self.my = self.start
        if self.my.key == orderId: 
            if self.start.value != None: 
                self.start = self.start.value
            else:
                self.start = None 
                self.end = None 
        else: 
            while self.my.value != None: 
                self.myNext = self.my.value
                if self.myNext.key == orderId: 
                    # 마지막인 경우 
                    if self.myNext.value == None: 
                        self.my.value = None 
                        self.end = self.my 
                    else:
                        self.my.value = self.myNext.value 
                else:
                    self.my = self.myNext 
        

    def getOrder(self, orderId) :
        '''
        주문번호 orderId가 몇 번째로 처리될지를 반환합니다.

        만약 주문번호 orderId가 존재하지 않으면 -1을 반환합니다. 
        '''
        self.my = self.start
        if self.start.key == orderId: 
            return 1 
        idx = 2 
        while self.my.value != None: 
            self.myNext = self.my.value
            if self.myNext.key == orderId: 
                return idx  
            else:
                self.my = self.myNext 
                idx += 1
        return -1 
                
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
