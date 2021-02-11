# 이분탐색 - 통과 
# 참고자료 : https://claude-u.tistory.com/448
import sys
N, C = map(int, input().split())
house = [int(sys.stdin.readline()) for _ in range(N)]

# 특정 거리내의 공유기 설치 갯수
## 만약 이 숫자가 C보다 크면 거리를 늘리고 작으면 거리를 줄이는 형식 
def find(dist):
    cnt = 1
    cur_house = house[0]
    for i in range(1, N):
        if cur_house + dist <= house[i]: # 특정 거리내의 밖에 있으면 공유기를 설치 
            cnt += 1
            cur_house = house[i]
    return cnt 

house = sorted(house)
start, end = 1, house[-1] - house[0]

while start <= end: 
    mid = (start + end) // 2

    if find(mid) >= C: 
        start = mid + 1
        ans = mid  
    else:
        end = mid - 1
print(ans)

# 백트래킹 - 메모리 에러 
import sys
sys.setrecursionlimit(10000)
N, C = map(int, input().split())
myarr = []
for i in range(N):
    myarr.append(int(sys.stdin.readline()))
myarr = sorted(myarr)
result = []

def findmin(values):
    val = 1000000000
    for i in range(1, len(values)):
        val = min(val, values[i] - values[i-1])
    return val

def dfs(values):
    if len(values) == C:
        result.append(findmin(values))
        return 
    
    for i in range(myarr.index(values[-1]), len(myarr)): 
            dfs(values + [myarr[i]])

for i in myarr:
    dfs([i])
print(max(result))

# 완전 탐색 - 메모리 에러 
from itertools import combinations
import sys
N, C = map(int, input().split())
myarr = []
for i in range(N):
    myarr.append(int(sys.stdin.readline()))
result = 0 
for arr in list(combinations(myarr, C)):
    val = []
    for i in range(1, len(arr)):
        val.append(arr[i] - arr[i-1])
    if min(val) > result: 
        result = min(val)
print(result)
