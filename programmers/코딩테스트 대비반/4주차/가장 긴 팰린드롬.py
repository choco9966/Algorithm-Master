# 완전탐색
def check(s):
    return s == s[::-1]

def solution(s):
    answer = []
    for i in range(0, len(s)):
        for j in range(i+1, len(s)+1):
            if check(s[i:j]): 
                answer.append(j-i)                
    return max(answer)


# DP
from itertools import chain
def check(s):
    return s == s[::-1]

def solution(s):
    answer = [[0] * len(s) for c in range(len(s))]
    
    # 1자리수에 대한 경우 
    for i in range(len(s)): 
        answer[i][i] = 1
        
    # 2자리수에 대한 경우 
    for i in range(len(s)-1): 
        if s[i] == s[i+1]: 
            answer[i][i+1] = 2
    
    # 3자리수 이상에 대한 팰린드롬 (DP) 
    for i in range(len(s)-2, -1, -1):
        for j in range(i+2, len(s)):
            # answer[i+1][j-1] != 0 ~ "abca" 반례 
            if (s[i] == s[j]) and (answer[i+1][j-1] != 0): 
                answer[i][j] = answer[i+1][j-1] + 2
                
    return max(list(chain(*answer)))
