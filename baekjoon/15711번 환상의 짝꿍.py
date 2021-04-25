# 참고자료 : https://yuuj.tistory.com/158
import math, sys
T = 2000000
primes = []
s = [0, 0] + [1 for _ in range(T)]
for i in range(2, T+1):
    if s[i]: 
        primes.append(i)
        s[2*i::i] = [0] * len(s[2*i::i])

def isPrime(n):
    try:
        return s[n]
    except:
        for prime in primes: 
            if prime > n: 
                return 1
            elif n % prime == 0:
                return 0
        return 1

for i in range(int(input())):
    m, n = map(int, input().split())
    num = m+n
    if num < 4: 
        print("NO")
    elif num % 2 == 0: 
        print("YES")
    else:
        if isPrime(num-2) == 1: 
            print("YES")
        else:
            print("NO")
