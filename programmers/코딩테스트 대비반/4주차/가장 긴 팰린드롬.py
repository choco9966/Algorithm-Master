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
