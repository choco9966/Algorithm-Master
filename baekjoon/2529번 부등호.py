N = int(input())
arr = list(map(str, input().split()))
nums = [False for _ in range(0, 10)]

def check(value, num):
    if arr[len(value)-1] == '<':
        return int(value[-1]) < num 
    else:
        return int(value[-1]) > num 

def dfs(value):
    global result
    if len(value) == (N+1):
        result.append(value)
        return 
    
    for num in range(0, 10):
        if not nums[num] and check(value, num):
            nums[num] = True
            dfs(value + str(num))
            nums[num] = False

result = []
for i in range(0, 10):
    nums[i] = True
    dfs(str(i))
    nums[i] = False
print(result[-1])
print(result[0])
