import sys
from itertools import combinations

def GCD(x, y) :
    if y == 0 :
        return x
    else :
        return GCD(y, x%y)

for _ in range(int(input())):
    arr = list(map(int, input().split()))[1:]
    result = 0
    for i in list(combinations(arr, 2)):     
        result += GCD(i[0], i[1])
    print(result)