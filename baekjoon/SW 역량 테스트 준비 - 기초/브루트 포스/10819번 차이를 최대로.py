from itertools import permutations
def cal(arr):
    val = 0
    for i in range(0, len(arr)-1):
        val += abs(arr[i]-arr[i+1])
    return val

N = int(input())
arr = list(map(int, input().split()))

result = []
for i in list(permutations(arr, N)):
    result += [cal(i)]
print(max(result))