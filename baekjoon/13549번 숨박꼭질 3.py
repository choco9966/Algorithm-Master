# 초기값을 0이 아닌 값으로 넣어야 통과함 
## 처음에 0으로 넣어서 비교했는데 0 -> 0*2가 계속 반복되면서 queue가 계속 늘어나는 문제가 있었음
## num*2의 경우 appendleft로 넣어줘서 우선순위를 높여줌 
from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
DP = [-1 for _ in range(0, 100000+1)]
DP[N] = 0 
queue = deque([N])
while queue:
    num = queue.popleft()
    if num == K: 
        print(DP[num])
        break
    else:
        if 2*num <= 100000 and DP[num*2] == -1:
            DP[2*num] = DP[num]
            queue.appendleft(num*2)
        if num-1 >= 0 and DP[num-1] == -1: 
            DP[num-1] = DP[num] + 1
            queue.append(num-1)
        if num+1 <= 100000 and DP[num+1] == -1:
            DP[num+1] = DP[num] + 1
            queue.append(num+1)
