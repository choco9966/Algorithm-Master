def lcs(a, b):
    if a % b == 0: return b 
    else: return lcs(b, (a % b))

def solution(arr):
    answer = 1 
    for i in arr: answer = (answer * i) / lcs(answer, i)
    return answer
