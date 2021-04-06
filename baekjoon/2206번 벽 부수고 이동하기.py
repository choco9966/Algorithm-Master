from collections import deque 
import sys 

input = sys.stdin.readline 
# input_file = open('./input/2206.txt', 'r')
# input = input_file.readline 

def bfs():
    queue = deque([(0, 0, 0)])
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited[0][0] = [1, 1]
    # N , M 모두 1인경우 100% 부분에서 테스트 케이스 오류 발생 
    if N == 1 and M == 1:
        return 1 
    while queue:
        mem = queue.popleft()
        # z : 벽뿌순지에 대한 여부 
        x, y, z = mem[0], mem[1], mem[2]
        for delta in deltas: 
            new_x, new_y = x + delta[0], y + delta[1]
            # 도착시에 도착한 칸으로 이동한 만큼 +1 해줘야함 
            if new_x == N-1 and new_y == M-1: 
                return visited[x][y][z] + 1
            if new_x >= 0 and new_x < N and new_y >= 0 and new_y < M: 
                # 벽을 부수고 이동하는 경우, 그렇지 않은 경우 모두 찾아야 하기에 if 2개로 엮음 
                # z == 1인 메세지가 필요없음. 벽을 부수지 않고 이동할 수도 있기때문임 
                if visited[new_x][new_y][z] == 0 and matrix[new_x][new_y] == 0: 
                    visited[new_x][new_y][z] = visited[x][y][z]+1 
                    queue.append((new_x, new_y, z))     

                if visited[new_x][new_y][z] == 0 and matrix[new_x][new_y] == 1 and z == 0: 
                    # 여기서 실수가 있음 visited[new_x][new_y][z+1]에 더해지는 값은 visited[x][y][z] 임 (이번에 벽을 부순거지 지난번은 아님) 
                    visited[new_x][new_y][z+1] = visited[x][y][z]+1 
                    queue.append((new_x, new_y, z+1))
    return -1 
N, M = map(int, input().split())    
matrix = [list(map(int, list(input())[:-1])) for _ in range(N)]
print(bfs())
