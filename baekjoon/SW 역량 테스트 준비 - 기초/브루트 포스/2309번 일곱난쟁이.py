from itertools import combinations 
import sys # sys.stdin.readline()
arr = []
arr += [int(sys.stdin.readline()) for _ in range(9)]
for i in list(combinations(arr, 7)):
    if sum(i) == 100: 
        break

for j in sorted(i):
    print(j)