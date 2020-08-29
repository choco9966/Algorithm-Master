def solution(n):
    Table = [0 for c in range(n+1)]
    Table[1] = 1
    for i in range(2, n+1):
        Table[i] = (Table[i-1] + Table[i-2]) % 1234567

    return Table[i]
