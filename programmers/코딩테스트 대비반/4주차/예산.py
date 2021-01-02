from itertools import combinations

def solution(d, budget):
    answer = 0
    sum_budget = 0
    d.sort()
    if sum(d) <= budget:
        return len(d)
    elif d[0] > budget:
        return 0
    else:
        for i in range(len(d)):
            if sum_budget + d[i] <= budget:
                sum_budget += d[i]
                answer += 1
            else:
                return answer


from collections import deque 
def solution(d, budget):
    n = len(d)
    d = deque(sorted(d))
    total = d.popleft()
    # 예산에 만족하는 부서가 하나도 없을 경우 (테스트 케이스3)
    if total > budget: 
        return 0
    else:
        while d:
            if total + d[0] <= budget: 
                total += d.popleft()
            else:
                break
        return n - len(d)
