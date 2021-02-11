# 이분 탐색 - 통과 (pyp3으로 제출)
# 참고자료 : https://claude-u.tistory.com/446
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)

start, end = 1, max(arr)
while start <= end:
    num = (start + end)//2
    result = 0
    for tree in arr: 
        if num < tree: 
            result += (tree - num)
        else:
            break

    if result >= M: 
        start = num + 1
    else:
        end = num - 1
print(end)

# 완전 탐색 - 시간초과 
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
nums = sorted(set(arr), reverse=True)

def lastindex(mylist, value):
    return len(mylist) - mylist[::-1].index(value) - 1

for num in nums: 
    idx = lastindex(arr, num)
    if sum(arr[:idx]) - (idx * arr[idx]) >= M:
        max_num = arr[idx]
        result = sum(arr[:idx]) - (idx * num)
        break 

for num in range(arr[idx-1]-1, arr[idx], -1):
    if sum(arr[:idx]) - (idx * num) >= M:
        max_num = num
        break

print(max_num)
