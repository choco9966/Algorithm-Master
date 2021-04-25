

# DFS와 BFS 분류

| 시간 제한 | 메모리 제한 | 제출   | 정답  | 맞은 사람 | 정답 비율 |
| :-------- | :---------- | :----- | :---- | :-------- | :-------- |
| 2 초      | 128 MB      | 115444 | 40199 | 23115     | 33.114%   |

## 문제

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

## 입력

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

## 출력

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

## 예제 입력 1 

```
4 5 1
1 2
1 3
1 4
2 4
3 4
```

## 예제 출력 1 

```
1 2 4 3
1 2 3 4
```

## 예제 입력 2 

```
5 5 3
5 4
5 2
1 2
3 4
3 1
```

## 예제 출력 2 

```
3 1 2 5 4
3 1 4 2 5
```

## 예제 입력 3 

```
1000 1 1000
999 1000
```

## 예제 출력 3 

```
1000 999
1000 999
```

## 풀이 

```python
import sys, copy
from collections import deque
# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split(' '))

tree = [[] for i in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split(' '))
    tree[i].append(j)
    tree[j].append(i)
# 문제중에 노드가 여러개인 경우에 대해서는 작은순서대로 출력이 되어야한다고 했음 
for i in range(N+1): 
    tree[i] = sorted(tree[i], reverse=True)

dfs_tree = copy.deepcopy(tree)
q = deque([V])
bfs = []
# BFS 
while len(q) > 0: 
    parent = q.popleft()
    bfs.append(parent)
    while len(tree[parent]) > 0: 
        i = tree[parent].pop()
        if (i not in bfs) & (i not in q): 
            q.append(i)


def finddfs(tree, v, result): 
    result.append(v) 
    while len(tree[v]) > 0:
        w = tree[v].pop()
        if w not in result: 
            result = finddfs(tree, w, result)
    return result
result = []
dfs = finddfs(dfs_tree, V, result)
print(' '.join(list(map(str, dfs))))
print(' '.join(list(map(str, bfs))))
```

## 다른사람 풀이 

- [[파이썬] 백준 1260번 DFS와 BFS by 코딩생활 커딩왕(차밍이)](https://chancoding.tistory.com/59)

```python
from sys import stdin
n, m, v = map(int, stdin.readline().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    line = list(map(int, stdin.readline().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1

def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        n = queue.pop(0)
        for c in range(len(matrix[start])):
            if matrix[n][c] == 1 and (c not in visited):
                visited.append(c)
                queue.append(c)
    return visited

def dfs(start, visited):
    visited += [start]
    for c in range(len(matrix[start])):
        if matrix[start][c] == 1 and (c not in visited):
            dfs(c, visited)
    return visited

print(*dfs(v,[]))
print(*bfs(v))
```



