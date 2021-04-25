# 해결 
## DP[num][1]에 경로를 저장하는게 아니라 바로 이전의 위치를 저장 
from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
DP = [[-1, -1] for _ in range(0, 100000+1)]
queue = deque([N])
result = deque([])
DP[N][0] = 0
while queue:
    num = queue.popleft()
    if num == K: 
        print(DP[num][0])
        result.appendleft(K)
        while DP[num][1] != -1:
            result.appendleft(DP[num][1])
            num = DP[num][1]
        print(' '.join(list(map(str, result))))
        sys.exit()
    else:
        if num-1 >= 0 and DP[num-1][0] == -1: 
            DP[num-1][0] = DP[num][0] + 1
            DP[num-1][1] = num
            queue.append(num-1)
        if num+1 <= 100000 and DP[num+1][0] == -1:
            DP[num+1][0] = DP[num][0] + 1
            DP[num+1][1] = num
            queue.append(num+1)
        if 2*num <= 100000 and DP[num*2][0] == -1:
            DP[2*num][0] = DP[num][0] + 1
            DP[2*num][1] = num
            queue.appendleft(num*2)

# 메모리 초과된 풀이 
## DP[num][1] 부분에 경로를 저장하기 -> 경로가 너무 길어짐에 따라 메모리 초과가 발생 
from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
DP = [[-1, []] for _ in range(0, 100000+1)]
queue = deque([N])
DP[N][0] = 0
while queue:
    num = queue.popleft()
    if num == K: 
        DP[num][1].append(num)
        print(DP[num][0])
        print(' '.join(map(str, DP[num][1])))
        sys.exit()
    else:
        if num-1 >= 0 and DP[num-1][0] == -1: 
            DP[num-1][0] = DP[num][0] + 1
            DP[num-1][1] = DP[num][1] + [num]
            queue.append(num-1)
        if num+1 <= 100000 and DP[num+1][0] == -1:
            DP[num+1][0] = DP[num][0] + 1
            DP[num+1][1] = DP[num][1] + [num]
            queue.append(num+1)
        if 2*num <= 100000 and DP[num*2][0] == -1:
            DP[2*num][0] = DP[num][0] + 1
            DP[2*num][1] = DP[num][1] + [num]
            queue.appendleft(num*2)
