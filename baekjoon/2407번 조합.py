N, M = map(int, input().split())
result = 1
for i, j in enumerate(range(N, N-M, -1)): 
    result *= j
    result //= (i+1)
print(result)
