'''
시간초과 
'''
def solution(n):
    DP = [c for c in range(0, n)]
    DP[0] = 1
    DP[1] = 2
    for i in range(2, n):
        DP[i] = DP[i-1] + DP[i-2]
    return DP[n-1] % 1000000007

'''
DP에 저장을 안하고 바로 직전의 2개 값만 저장 
'''
def solution(n):
    i_1 = 2; i_2 = 1; 
    for _ in range(3, n+1):
        i_1, i_2 = i_1 + i_2, i_1
    return i_1 % 1000000007
