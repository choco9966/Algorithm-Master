# 수정된 풀이 
## power의 계산을 분할정복을 통해서 계산 
## % c의 경우 return시에 미리 해줌 (이게 없고에 따라서 속도 차이가 꽤 발생함)
def power(n, m):
    if m == 1: 
        return n % c
    else:
        temp = power(n, m//2)
        if m % 2 == 0: 
            return temp * temp % c
        else:
            return temp * temp * a % c

a, b, c = map(int, input().split())
print(power(a, b))

# 시간초과 
a, b, c = map(int, input().split())
print((a**b)%c)
