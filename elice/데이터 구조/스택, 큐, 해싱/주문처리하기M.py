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
        if len(self.myQueue) == 0 :
            return -1
        else :
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

class orderInfo:
    '''
    이 부분은 수정하지 마세요.
    '''
    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v

def selectQueue(normalQueue, vipQueue, jobEndTime, orders) :
    normalIdx = normalQueue.front()
    vipIdx = vipQueue.front()

    if vipIdx == -1 :
        return normalQueue

    if normalIdx == -1 :
        return vipQueue

    minQueue = -1
    maxQueue = -1

    if normalIdx < vipIdx :
        minQueue = normalQueue
        maxQueue = vipQueue
    else :
        minQueue = vipQueue
        maxQueue = normalQueue
        
    maxIdx = max(normalIdx, vipIdx)

    if min(jobEndTime) < orders[maxIdx].time :
        return minQueue
    else :
        return vipQueue

def selectWorker(jobEndTime, orderIdx, orders) :
    if min(jobEndTime) <= orders[orderIdx].time :
        for i in range(len(jobEndTime)) :
            if jobEndTime[i] <= orders[orderIdx].time :
                return i
    else :
        minValue = min(jobEndTime)

        for i in range(len(jobEndTime)) :
            if minValue == jobEndTime[i] :
                return i
        
def processOrder(orders, m) :
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 출력합니다.
    '''

    result = [ [] for i in range(m) ] 

    normalQueue = Queue()
    vipQueue = Queue()

    jobEndTime = [ 0 for i in range(m) ]
    curTime = -1

    for i in range(len(orders)) :
        if orders[i].vip == 0 :
            normalQueue.push(i)
        else :
            vipQueue.push(i)

    while not(normalQueue.empty() == 1 and vipQueue.empty() == 1) :
        targetQueue = selectQueue(normalQueue, vipQueue, jobEndTime, orders)

        idx = targetQueue.front()
        workerIdx = selectWorker(jobEndTime, idx, orders)

        jobEndTime[workerIdx] = max(jobEndTime[workerIdx], orders[idx].time) + orders[idx].duration

        result[workerIdx].append(idx + 1)
        targetQueue.pop()

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    p = [int(v) for v in input().split()]

    orders = []

    for i in range(p[0]) :
        myList = [int(v) for v in input().split()]

        orders.append(orderInfo(myList[0], myList[1], myList[2]))

    ans = processOrder(orders, p[1])

    for i in range(len(ans)) :
        print(*ans[i])

if __name__ == "__main__":
    main()
