# 1003 피보나치 함수 
'''
시간초과 
'''
import sys 
input = sys.stdin.readline 

def fibonacci(n): 
    global zero
    global one 
    if n == 0: 
        zero += 1 
        return 0 
    elif n == 1: 
        one += 1 
        return 1 
    else: 
        return (fibonacci(n-1) + fibonacci(n-2))
    
for _ in range(int(input())): 
    zero, one = 0, 0 
    fibonacci(int(input()))
    print(zero, one)

'''
DP 이용한 접근 
'''
import sys
input = sys.stdin.readline 
DP = [[0, 0] for c in range(40+1)]
DP[0] = [1, 0]
DP[1] = [0, 1]

N = int(input())
case = []
for _ in range(N):
    case.append(int(sys.stdin.readline()))

for i in range(2, max(case)+1): 
    DP[i] = [DP[i-1][0] + DP[i-2][0], DP[i-1][1] + DP[i-2][1]]

for i in case: 
    print(' '.join(list(map(str, DP[i]))))
