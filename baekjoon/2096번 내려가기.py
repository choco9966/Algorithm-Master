import sys, copy 
input = sys.stdin.readline 
n = int(input()) 
large, small = [0, 0, 0], [0, 0, 0]
for i in range(n): 
    table = list(map(int, input().split()))
    large = [max(large[0], large[1]) + table[0], max(large[0], large[1], large[2]) + table[1], max(large[1], large[2]) + table[2]] 
    small = [min(small[0], small[1]) + table[0], min(small[0], small[1], small[2]) + table[1], min(small[1], small[2]) + table[2]] 
print(max(large), min(small))
