from collections import Counter
def two_change(n):
    if n == 0: return ''
    elif n % 2 == 0: return two_change(n//2) + '0'
    else: return two_change(n//2) + '1'

def count_one(n):
    n = two_change(n)
    n = Counter(list(n))
    return n['1']

def solution(n):
    cnt = count_one(n)
    for i in range(n+1, 1000001): 
    # 1. n의 2진수시에 1의 갯수 확인 
        if cnt == (count_one(i)): return i 
