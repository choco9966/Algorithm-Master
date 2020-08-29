def solution(heights):
    answer = []
    for i in range(len(heights)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                answer.append((j+1))
                break
        # 자기보다 큰게 없는 경우, 단 첫번째 탑이 신호를 수신한 경우가 아니어야함  
        if (j == 0) & (heights[i] >= heights[j]):
        # if (len(answer) != (len(heights) - i)):
            answer.append(0)
            
    
    solution = []
    while len(answer) > 0: 
        solution.append(answer.pop())

    return solution
