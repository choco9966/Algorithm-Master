from queue import PriorityQueue
def getMinForce(weights) :
    '''
    n개의 점토를 하나로 합치기 위해 필요한 힘의 합의 최솟값을 반환하는 함수를 작성하세요.
    '''
    weight_queue = PriorityQueue()
    for i in weights: 
        weight_queue.put(i)
    result = 0
    
    while weight_queue.qsize() > 1: 
        x1 = weight_queue.get()
        x2 = weight_queue.get() 
        x3 = x1 + x2
        result += x3
        weight_queue.put(x3)
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
