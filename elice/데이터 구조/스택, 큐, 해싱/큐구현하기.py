class Queue:
    '''
    List를 이용하여 다음의 method들을 작성하세요.
    '''
    def __init__(self) :
        '''
        큐 myQueue을 만듭니다.
        '''
        self.myQueue = []

    def push(self, n) :
        '''
        queue에 n을 넣습니다.
        '''
        self.myQueue.append(n)

    def pop(self) :
        '''
        queue에서 가장 앞에 있는 값을 제거하고, 그 수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if len(self.myQueue) != 0 :
            result = self.myQueue[0]
            del self.myQueue[0]

    def size(self) :
        '''
        queue에 들어 있는 값의 개수를 return 합니다.
        '''
        return len(self.myQueue)

    def empty(self) :
        '''
        queue이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        if len(self.myQueue) == 0 :
            return 1
        else :
            return 0

    def front(self) :
        '''
        queue의 가장 앞에 있는 값을 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if len(self.myQueue) == 0 :
            return -1
        else :
            return self.myQueue[0]

    def back(self) :
        '''
        queue의 가장 뒤에 있는 값을 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if len(self.myQueue) == 0 :
            return -1
        else :
            return self.myQueue[len(self.myQueue)-1]




def main():
    queue = Queue()

    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''
    queue.push(1)
    queue.push(2)
    queue.pop()
    queue.push(4)
    queue.pop()


    print(queue.size()) 
    print(queue.front())
    print(queue.empty())


if __name__ == "__main__":
    main()