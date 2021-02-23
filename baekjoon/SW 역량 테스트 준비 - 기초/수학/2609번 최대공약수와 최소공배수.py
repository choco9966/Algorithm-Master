# 방법1. GCD 함수 이용 
import sys
def GCD(x, y) :
    if y == 0 :
        return x
    else :
        return GCD(y, x%y)

n1, n2 = map(int, input().split())
gcd = GCD(n1, n2)
print(gcd)
print(gcd * (n1//gcd) * (n2//gcd))

# 방법2. FOR문으로 계산하는 방법 
import sys
n1, n2 = map(int, input().split())
result = []
for i in range(1, max(n1, n2)+1):
    if n1 % i == 0 and n2 % i == 0: 
        result.append(i)
print(result[-1])
print(result[-1] * (n1//result[-1]) * (n2//result[-1]))