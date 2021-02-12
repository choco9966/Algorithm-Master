import sys
n1, n2 = map(int, input().split())
result = []
for i in range(1, max(n1, n2)+1):
    if n1 % i == 0 and n2 % i == 0: 
        result.append(i)
print(result[-1])
print(result[-1] * (n1//result[-1]) * (n2//result[-1]))
