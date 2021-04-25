E, S, M = map(int, input().split()) # 지구, 태양, 달
e, s, m, cnt = 1, 1, 1, 1
while not (e == E and s == S and m == M): 
    e, s, m, cnt = e+1, s+1, m+1, cnt+1
    if e >= 15+1: e = 1
    if s >= 28+1: s = 1
    if m >= 19+1: m = 1
print(cnt)