# 출처 : https://namhandong.tistory.com/113
import sys 
s1 = list(sys.stdin.readline().strip())
s2 = []
m = int(sys.stdin.readline())
n = len(s1)

for i in range(m):
    com = sys.stdin.readline().strip()
    if com[0] == 'P':
        s1.append(com[2])
    elif com[0] == 'L' and s1 != []: 
        s2.append(s1.pop())
    elif com[0] == 'D' and s2 != []:
        s1.append(s2.pop())
    elif com[0] == 'B' and s1 != []: 
        s1.pop()
print("".join(s1 + list(reversed(s2))))

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
