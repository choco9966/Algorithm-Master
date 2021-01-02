from itertools import combinations
import math 

def find(n): 
    s = [0, 0] + [1] * (n-1)
    for i in range(2, int(math.sqrt(n))+1): 
        s[2*i::i] = [0] * ((n - i)//i)
    return s

def solution(nums):
    answer = 0
    nums = list(map(sum, combinations(nums, 3)))
    s = find(max(nums)) 
    for i in nums: 
        if s[i] == 1: 
            answer += 1    
    return answer
