class priorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''

    def __init__(self) :
        self.data = [0]

    def push(self, value) :
        '''
        우선순위 큐에 value를 삽입합니다
        '''
        self.data.append(value)
        idx = len(self.data) - 1
        while idx > 0 :
            if self.data[idx//2] > self.data[idx] :
                self.data[idx],self.data[idx//2] = self.data[idx//2],self.data[idx]
                idx = idx // 2
            else :
                break

    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다
        '''
        if len(self.data) == 1 :
            return -1
        else :
            return self.data[1]

    def pop(self) :
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''
        if len(self.data) != 1 :
            self.data[1] = self.data[len(self.data)-1]
            self.data.pop()
            idx = 1
            data_size = len(self.data)
            while idx < data_size :
                swap_idx = idx * 2
                if swap_idx+1 < data_size and self.data[idx*2] > self.data[idx*2+1] :
                    swap_idx += 1
                if swap_idx < data_size and self.data[swap_idx] < self.data[idx] :
                    self.data[swap_idx],self.data[idx] = self.data[idx],self.data[swap_idx]
                    idx = swap_idx
                else :
                    break

def getMinForce(weights) :
    '''
    n개의 점토를 하나로 합치기 위해 필요한 힘의 합의 최솟값을 반환하는 함수를 작성하세요.
    '''

    result = 0
    myPQ = priorityQueue()
    
    for weight in weights :
        myPQ.push(weight)
    while True :
        if myPQ.top() == -1 :
            break
        a = myPQ.top()
        myPQ.pop()
        b = myPQ.top()
        myPQ.pop()
        if b == -1 : 
            break
        result += a + b
        myPQ.push(a+b)
    
    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    line = [int(x) for x in input().split()]

    print (getMinForce(line))

if __name__ == '__main__':
    main()
