# 참고자료 : https://inspirit941.tistory.com/200
import heapq
import sys, math

N = int(input())
# heap을 2개 생성해서 길이를 기준으로 왼쪽과 오른쪽을 맞춤 
## 단, 중심의 경우 왼쪽에 저장한 후에 크기비교를 하는 형식 
## 이렇게 해주는 이유는 왼쪽의 마지막에서 하나를 출력하기 위함 
left, right = [], []
for _ in range(N):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))
    
    if right and left[0][1] > right[0][1]: 
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(right, (left_value, left_value))
        heapq.heappush(left, (-right_value, right_value))
    sys.stdout.write(f'{left[0][1]}'+'\n')
