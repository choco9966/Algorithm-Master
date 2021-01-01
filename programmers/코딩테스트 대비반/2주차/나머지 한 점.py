from collections import Counter
def solution(v):
    x, y = [], []
    for i in v:
        x.append(i[0])
        y.append(i[1])

    x = sorted(Counter(x).items(), key=lambda x: x[1])[0][0]
    y = sorted(Counter(y).items(), key=lambda x: x[1])[0][0]
    return [x, y]
