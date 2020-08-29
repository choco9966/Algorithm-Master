def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for c in range(bridge_length)]

    timer = 0
    while len(truck_weights) > 0:
        # print(bridge, truck_weights, timer)
        if sum(bridge[1:]) + truck_weights[0] <= weight:
            bridge.append(truck_weights[0])
            truck_weights.pop(0)
        else:
            # 앞에 0인 값들 한개 빼고 모두 제거 
            while bridge[1] == 0:
                bridge.pop(0)
                bridge.append(0)
                timer += 1
            bridge.append(0)

        timer += 1
        bridge.pop(0)


    # 남아있는 트럭에 대해 계산 
    timer += len(bridge)            
    return timer
