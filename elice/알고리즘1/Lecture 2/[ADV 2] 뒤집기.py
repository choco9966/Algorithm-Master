import sys
import copy
sys.setrecursionlimit(100000)

def powerSetInternal(temp, n) :
    result = []

    if len(temp) == 0 :
        for i in range(1, n+1) :
            result.append([i])

            temp.append(i)
            result = result + powerSetInternal(temp, n)
            temp.pop()
    else :
        last = temp[-1]

        for i in range(last+1, n+1) :
            temp.append(i)
            result.append(list(temp))

            result = result + powerSetInternal(temp, n)
            temp.pop()

    return result

def singleFlip(myMap, y, x, n, m) :
    dy = [-1, 0, 0, 0, 1]
    dx = [0, -1, 0, 1, 0]

    for k in range(len(dy)) :
        yy = y + dy[k]
        xx = x + dx[k]

        if yy >= 0 and yy < n and xx >= 0 and xx < m :
            myMap[yy][xx] = 1 - myMap[yy][xx]

    return myMap

def isPossible(myMap, assignment) :
    cnt = 0 

    n = len(myMap)
    m = len(myMap[0])

    for x in assignment :
        singleFlip(myMap, 0, x-1, n, m)
        cnt += 1

    for i in range(1, n) :
        for j in range(m) :
            if myMap[i-1][j] == 1 :
                singleFlip(myMap, i, j, n, m)
                cnt += 1

    for j in range(m) :
        if myMap[n-1][j] == 1 :
            return -1

    return cnt

def flip(myMap, n, m) :
    '''
    모든 칸을 흰색으로 바꾸기 위해 최소로 클릭해야 하는 횟수를 반환하는 함수를 작성하세요.
    '''

    combinations = [[]] + powerSetInternal([], m)
    cnt = n * m + 1

    for assignment in combinations :
        localCnt = isPossible(copy.deepcopy(myMap), assignment)

        if localCnt != -1 :
            cnt = min(cnt, localCnt)

    if cnt == n * m + 1 :
        return -1
    else :
        return cnt

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    n = data[0]
    m = data[1]

    myMap = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        myMap.append(line)

    print(flip(myMap, n, m))

if __name__ == "__main__":
    main()