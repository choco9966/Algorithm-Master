N, M, V = map(int, input().split())
if (V-M) % (N-M) == 0:
    print((V-M) // (N-M))
else:
    print((V-M) // (N-M) +1)
