# 참고자료 : https://claude-u.tistory.com/360
## 비슷한 방식인데 후보를 미리 찾고 해당 영역만 계산하는 것으로 수정된 풀이 
## 1. 후보를 미리 candidate 함수를 통해서 찾음 
## 2. zero인 부분을 모두 조사해서 해당 영역에 대해서만 계산 
## 3. pypy3으로 제출해야 통과함 
from itertools import chain
def candidate(i, j): 
    numbers = [c for c in range(1, 10)]
    
    for k in range(0, 9):
        if matrix[i][k] in numbers:
            numbers.remove(matrix[i][k])
        if matrix[k][j] in numbers:
            numbers.remove(matrix[k][j])
    
    start_i = i // 3
    start_j = j // 3
    for dx in range(start_i * 3, (start_i+1) * 3):
        for dy in range(start_j * 3, (start_j+1) * 3):
            if matrix[dx][dy] in numbers:
                numbers.remove(matrix[dx][dy])
    
    return numbers

def backtracking(idx):
    global flag 
    if flag == True: 
        return 
    
    if len(zeros) == idx:
        for i in range(9):
            print(' '.join(list(map(str, matrix[i]))))
        flag = True
        return
    else:
        (i, j) = zeros[idx]
        candidate_list = candidate(i, j)
        for num in candidate_list:
            matrix[i][j] = num
            backtracking(idx + 1)
            # 답이 없는 경우 
            matrix[i][j] = 0
    
matrix = [list(map(int, input().split())) for _ in range(9)]
zeros = [(x, y) for x in range(9) for y in range(9) if matrix[x][y] == 0]
flag = False
backtracking(0)

# 백트래킹 - 시간초과 
from itertools import chain
def check(matrix, num, x, y):
    if num not in matrix[x]: # 같은 행에 중복이 없음 
        for x1 in range(3*(x//3), 3*(x//3)+3):
            for y1 in range(3*(y//3), 3*(y//3)+3):
                if matrix[x1][y1] == num: 
                    return False
        return True
    else:
        return False

def backtracking(x, y):
    global flag 
    if flag == True or x == 9: 
        return 

    if 0 not in set(chain(*matrix)): 
        for i in range(9):
            print(' '.join(list(map(str, matrix[i]))))
        flag = True
        return

    for new_y in range(y, 9):
        if matrix[x][new_y] == 0:
            for num in range(1, 10): 
                if check(matrix, num, x, new_y):
                    matrix[x][new_y] = num
                    backtracking(x, new_y)
                    matrix[x][new_y] = 0
    backtracking(x+1, 0)
matrix = [list(map(int, input().split())) for _ in range(9)]
flag = False
backtracking(0, 0)
