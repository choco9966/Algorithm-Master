def solution(A,B):
    answer = 0
    A.sort()
    B = sorted(B, reverse = True)

    # 작은값과 큰값을 곱해야 합이 제일 작음 
    for i in range(len(A)):
        answer += A[i] * B[i]
    
    return answer
