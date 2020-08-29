def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)

    answer = sum([a * b for a, b in zip(A, B)])
    return answer
