'''
경로에 웅덩이가 겹치는 경우 계산이 안되는 문제가 있음 
'''
def solution(m, n, puddles):
    F = [0 for c in range(200+1)]
    F[0] = 1; F[1] = 1
    for i in range(2, 201):
        F[i] = F[i-1] * i

    # 전체 경우의 수 
    answer = F[m+n-2] / (F[m-1] * F[n-1])
    
    # 웅덩이에 갔다가 학교에 가는 경우의 수 
    for i in puddles: 
        # puddle까지 가는 경우의 수 * puddle에서 학교까지 가는 경우의 수
        answer -= (F[i[0]+i[1]-2] / (F[i[0]-1] * F[i[1]-1])) * (F[m-i[0] + n-i[1]] / (F[m-i[0]] * F[n-i[1]]))
    return answer % 1000000007


'''
수정된 풀이 
'''
def solution(m, n, puddles):
    table = [[0] * (m+1) for _ in range(n+1)]
    table[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] in puddles: 
                table[i][j] = 0
            else:
                # 자기자신이 어차피 0이어서 더해줘도 상관없음 
                ## 자기자신 더하는걸 빼면 에러가 발생하는 이유는 [1, 1] 집의 시작점이 0으로 바뀌기 때문 
                table[i][j] += table[i][j-1] + table[i-1][j]
    return table[n][m] % 1000000007
