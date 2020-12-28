from heapq import heappush, heappop

class priorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''

    def __init__(self) :
        self.data = []

    def push(self, value) :
        '''
        우선순위 큐에 value를 삽입합니다.
        '''
        heappush(self.data, value)

    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다. 
        만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''
        if len(self.data) <= 0 :
            return -1
        else :
            return self.data[0]
        

    def pop(self) :
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''
        if len(self.data) <= 0 :
            return
        else :
            heappop(self.data)
        

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
