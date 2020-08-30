def solution(s):
    answer = []
    s = s[2:-2]
    s = sorted(s.split("},{"), key = lambda x: len(x))

    for i in s:
        i_ = i.split(',')
        for j in i_:
            if int(j) not in answer:
                answer.append(int(j))
    return answer
