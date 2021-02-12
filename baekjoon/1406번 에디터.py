# 시간초과 
import sys
from collections import deque
mess = str(input())
N = int(input())
input = sys.stdin.readline
idx = len(mess)
for _ in range(N):
    m = list(map(str,input().split()))   
    if m[0] == 'L':
        idx -= 1
        if idx <= 0: idx = 0
    elif m[0] == 'D':
        idx += 1
        if idx >= len(mess): idx = len(mess)
    elif m[0] == 'B':
        if idx == 0: 
            pass 
        else:
            if idx == len(mess):
                mess = mess[0:idx-1]
            else:
                mess = mess[0:idx-1] + mess[idx:]
            idx -=1
    else:
        if idx == len(mess):
            mess = mess[0:idx] + m[1]
        else:
            mess = mess[0:idx] + m[1] + mess[idx:]
        idx += 1
print(mess)
