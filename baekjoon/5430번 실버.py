import re
from collections import deque
T = int(input())
def solve(com, arr):
    switch = 0 # 왼쪽 
    if arr == deque(['']):
        arr = deque([])
    for c in com: 
        if c == 'R': 
            switch += 1
        else:
            if switch % 2 == 0:
                try: 
                    arr.popleft()
                except:
                    print('error')
                    return
            else:
                try: 
                    arr.pop()
                except:
                    print('error')
                    return
    if switch % 2 == 0: 
        arr = list(arr)
    else:
        arr = list(reversed(arr))
    print("[", end = "") 
    print(",".join(arr), end = "") 
    print("]")
    return

for _ in range(T): 
    com = str(input().strip())
    n = int(input())
    arr = re.split("\[|\]|,|\n", input()) 
    arr = deque(arr[1:-1])
    solve(com, arr)
