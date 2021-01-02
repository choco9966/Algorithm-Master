# Run Time Error 코드
def solution(budgets, M):
    answer = []
    k = min(budgets)
    n = max(budgets)
    for i in range(k, n+1):
        a, b = i, sum([i if c >= i else c for c in budgets])
        if b <= M:
            answer.append((a, b))
    return sorted(answer, key = lambda x: -x[1])[0][0]


def solution(budgets, M):
    left, right = 0, max(budgets)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        temp = [i if i < mid else mid for i in budgets]
        if sum(temp) > M:
            right = mid-1
        elif sum(temp) <= M:
            answer = mid
            left = mid+1
    return answer
