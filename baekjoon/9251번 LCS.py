L1 = list(input())
L2 = list(input())
matrix = [[0 for _ in range(len(L2)+1)] for _ in range(len(L1)+1)]
for i in range(1, len(L1)+1):
    for j in range(1, len(L2)+1):
        if L1[i-1] == L2[j-1]: 
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
print(matrix[-1][-1])
