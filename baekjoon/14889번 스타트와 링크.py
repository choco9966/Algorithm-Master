import sys
from itertools import combinations
from itertools import chain

input = sys.stdin.readline
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
numbers = [i for i in range(N)]

result = []
for comb in list(combinations(numbers, N//2))[0:len(list(combinations(numbers, N//2)))//2]:
    num1, num2 = 0, 0
    start_team = comb
    link_team = list(set(numbers).difference(set(start_team)))
    for idx in list(combinations(start_team, 2)):
        num1 += (matrix[idx[0]][idx[1]] + matrix[idx[1]][idx[0]])

    for idx in list(combinations(link_team, 2)):
        num2 += (matrix[idx[0]][idx[1]] + matrix[idx[1]][idx[0]])        
    result.append(abs(num1-num2))
print(min(result))
