from itertools import permutations
N = int(input())
for i in list(permutations([i for i in range(1, N+1)], N)):
    print(*i)