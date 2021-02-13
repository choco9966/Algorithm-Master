from itertools import permutations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
for i in sorted(set(permutations(arr, M))):
    print(*i)
