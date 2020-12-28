class priorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''

    def __init__(self) :
        self.data = [0]

    def push(self, value) :
        '''
        우선순위 큐에 value를 삽입합니다.
        '''
        self.data.append(value)
        
        index = len(self.data) - 1
        
        while index != 1:
            if self.data[index//2] > self.data[index]:
                temp = self.data[index]
                self.data[index] = self.data[index//2]
                self.data[index//2] = temp
                
                index = index//2
            else:
                break


    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''
        if len(self.data) == 1:
            return -1
        else :
            return self.data[1]


    def pop(self) :
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''
        if len(self.data) == 1:
            return
        
        self.data[1] = self.data[-1]
        self.data.pop()
        
        index = 1
        
        while True:
            priority = -1
            
            # 1 아무 자식도 없는 경우
            if len(self.data)-1 < index * 2:
                break
            # 2 오직 왼쪽 자식만 있는 경우
            elif len(self.data) - 1 < index * 2 + 1:
                priority = index * 2
            else:
                if self.data[index*2] < self.data[index*2+1]:
                    priority = index * 2
                else:
                    priority = index * 2 +1
            
            if self.data[index] > self.data[priority]:
                temp = self.data[index]
                self.data[index] = self.data[priority]
                self.data[priority] = temp
                
                index = priority
            else:
                break


def main():
    myPQ = priorityQueue()

    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    myPQ.push(1)
    myPQ.push(4)
    myPQ.push(3)
    myPQ.push(2)

    print(myPQ.top())
    myPQ.pop()

    print(myPQ.top())
    myPQ.pop()

if __name__ == "__main__":
    main()