# 참고자료 : https://claude-u.tistory.com/427
# 해결 : 미리 summatation된 Matrix를 계산하고 값을 추출 
## 예) matrix[x][y] = 0, 0에서부터 x, y까지의 summation을 미리 계산한 부분 
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            pass
        elif i == 0:            
            matrix[0][j] += matrix[0][j-1]
        elif j == 0:
            matrix[i][0] += matrix[i-1][0]
        else:
            matrix[i][j] += (matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1])

#예외 처리(i-2, j-2가 안되는 경우) 해주고 정답 출력
for _ in range(M):
    i, j, x, y = map(int, sys.stdin.readline().split())
    if i == 1 and j == 1:
        print(matrix[x-1][y-1])
    elif i == 1:
        print(matrix[x-1][y-1] - matrix[x-1][j-2])
    elif j == 1:
        print(matrix[x-1][y-1] - matrix[i-2][y-1])
    else:
        print(matrix[x-1][y-1] - matrix[i-2][y-1] - matrix[x-1][j-2] + matrix[i-2][j-2])
        
# 시간초과 
## result를 계산해서 summation을 하는 부분이 시간이 오래걸림 
import sys
from itertools import chain
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    # matrix가 0번 인덱스부터 시작하니 1을 제거해줌 
    result = [row[y1-1:y2] for row in matrix[x1-1:x2]]
    sys.stdout.write(f'{sum(chain(*result))}' + '\n')
