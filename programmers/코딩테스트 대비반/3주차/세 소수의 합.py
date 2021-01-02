from itertools import combinations
import math

def prime(t):
    cnt = 0
    s = [c for c in range(0, t+1)]
    for i in range(2, int(math.sqrt(t))+1):
        if s[i]:
            s[i*2::i] = [0] * ((t - i)//i)
    return [i for i in range(2, t) if s[i] != 0]

def solution(n):
    answer = 0
    prime_num = prime(n)
    
    comb_prime = combinations(prime_num, 3)
    
    for comb in comb_prime:
        if sum(comb) == int(n):
            answer += 1
            
    return answer
