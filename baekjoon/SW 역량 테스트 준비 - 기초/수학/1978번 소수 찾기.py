import math 
N = int(input())
a = [0, 0] + [1]*(1000-1) # 0과 1은 제외 
for i in range(2, int(math.sqrt(1000))+1): 
    for j in range(2*i, 1000+1, i): 
        a[j] = 0

answer = 0 
myList = list(map(int, input().split()))
for j in myList: 
    answer += a[j]
print(answer)