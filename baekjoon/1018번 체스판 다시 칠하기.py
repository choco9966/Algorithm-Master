col1 = ['W','B','W','B','W','B','W','B']
col2 = ['B','W','B','W','B','W','B','W']
mat1 = [col1 if i % 2 == 0 else col2 for i in range(0, 8)]
mat2 = [col1 if i % 2 != 0 else col2 for i in range(0, 8)]

def solve(chess):
    cnt1, cnt2 = 0, 0
    for row1, row2 in zip(chess, mat1):
        for x, y in zip(row1, row2):
            if x != y: cnt1 += 1

    for row1, row2 in zip(chess, mat2):
        for x, y in zip(row1, row2):
            if x != y: cnt2 += 1
    return min(cnt1, cnt2)

N, M = map(int, input().split())
matrix = [list(map(str, input().strip())) for _ in range(N)]

# 전체 경우 탐색 
result = []
for x in range(0, N-8+1):
    for y in range(0, M-8+1):
        chess = [row[y:y+8] for row in matrix[x:x+8]]
        result += [solve(chess)]
print(min(result))
