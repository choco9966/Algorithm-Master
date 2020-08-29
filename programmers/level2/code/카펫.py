def findvalue(total):
    answer = []
    for i in range(1, total+1):
        if total % i == 0: answer.append(i)
    return answer 

def solution(brown, red):
    total = brown + red
    sol = [0, 0]
    answer = findvalue(total)
    if len(answer) % 2 == 0: left = answer[0:len(answer)//2]; right = answer[len(answer)//2:]
    else: left = answer[0:1 + len(answer)//2]; right = answer[len(answer)//2:]
    for point in range(0, len(left)):
        if 2*(left[point] + right[len(left) - 1 - point])-4 == brown:
            return [right[len(left) - 1 - point], left[point]]
        else:
            continue 
    return answer
