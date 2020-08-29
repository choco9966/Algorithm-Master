def solution(s):
    answer = ''
    for idx, i in enumerate(s): 
        if (idx == 0): answer = i.upper()
        elif s[idx-1] == ' ': answer = ''.join([answer, i.upper()])
        else: answer = ''.join([answer, i.lower()])
    return answer
