from itertools import product 
def solution(monster, S1, S2, S3):
    answer = -1
    n = S1*S2*S3
    
    # 주사위의 최소값은 1이라고 가정 
    S1 = [c for c in range(1, S1+1)]
    S2 = [c for c in range(1, S2+1)]
    S3 = [c for c in range(1, S3+1)]
    
    # S1, S2, S3에 대해서 가능한 모든 경우의 수 계산 
    all_case = product(*[S1, S2, S3])
    
    monster_case = 0
    for i in all_case: 
        # +1은 별의 위치를 의미 
        if sum(i) + 1 in monster: monster_case += 1 
    
    answer = int(1000 * ((n - monster_case) / n))
    return answer
