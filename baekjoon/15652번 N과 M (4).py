from itertools import combinations_with_replacement
N, M = map(int, input().split())
for i in list(combinations_with_replacement([c for c in range(1, N+1)],M)):
    print(*i)
