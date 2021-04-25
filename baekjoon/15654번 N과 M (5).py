from itertools import permutations

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
for i in list(permutations(arr, M)):
    print(' '.join(map(str, list(i))))
