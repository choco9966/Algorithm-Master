import sys 
# input = sys.stdin.readline
N, M = map(int, input().split())

id2num, num2id = {}, {}
for i in range(1, N+1):
    i = str(i)
    x = str(input().replace('\n', ''))
    id2num[x] = i
    num2id[i] = x

for i in range(M):
    x = str(input().replace('\n', ''))
    if x.isalpha(): print(id2num[x])
    else: print(num2id[x])
