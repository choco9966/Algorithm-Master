# deque 활용 
from collections import deque 
N = input()
p = deque(sorted(list(map(int, input().split()))))
result = []
cumsum = 0
while p: 
    result += [cumsum + p[0]]
    cumsum += p.popleft()
print(sum(result))

# 리스트 활용 
N = int(input())
myArray = list(map(int, input().split(' ')))

sol = 0
myArray = sorted(myArray)
for i in range(len(myArray)):
    sol += (myArray[i] * (N-i))
print(sol)
