class orderInfo:
    '''
    이 부분은 수정하지 마세요.
    '''
    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v

def selectQueue(orders, VIP, non_VIP, time):
    if len(VIP)==0 and len(non_VIP)>0:
        return non_VIP
    elif len(non_VIP)==0 and len(VIP)>0:
        return VIP
    else:
        if time < orders[VIP[0]].time and time < orders[non_VIP[0]].time:
            if orders[VIP[0]].time<=orders[non_VIP[0]].time:
                return VIP
            elif orders[VIP[0]].time>orders[non_VIP[0]].time:
                return non_VIP
            else:
                return -1
        else:
            if orders[VIP[0]].time <= time:
                return VIP
            elif orders[non_VIP[0]].time <= time:
                return non_VIP
            else:
                return -1

def processOrder(orders) :
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 출력합니다.
    '''
    if len(orders)==0:
        return 0
    
    result = []
    time = 0
    VIP = []
    non_VIP = []
    
    for i in range(len(orders)):
        if orders[i].vip==1:
            VIP.append(i)
        else:
            non_VIP.append(i)
    while not (len(VIP)==0 and len(non_VIP)==0):
        which = selectQueue(orders, VIP, non_VIP, time)
        idx = which.pop(0)
        time = max(time, orders[idx].time) + orders[idx].duration
        result.append(idx+1)
    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    p = int(input())

    orders = []

    for i in range(p) :
        myList = [int(v) for v in input().split()]

        orders.append(orderInfo(myList[0], myList[1], myList[2]))

    print(*processOrder(orders))

if __name__ == "__main__":
    main()

