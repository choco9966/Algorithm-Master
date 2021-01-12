import sys
sys.setrecursionlimit(100000)

def quickSort(array) :
    if len(array) < 2 :
        return array
    pivot = array[len(array)//2]
    left = []
    right = []
    equal = []
    for x in array :
        if abs(pivot) > abs(x) :
            left.append(x)
        elif abs(pivot) < abs(x) :
            right.append(x)
        else :
            if x < 0 :
                equal = [x] + equal
            else :
                equal.append(x)
    return quickSort(left) + equal + quickSort(right)

def sortAbs(array):
    '''
    절댓값을 기준으로 오름차순 정렬한 결과를 반환하는 함수를 작성하세요.
    '''
    return quickSort(array)

def main():
    line = [int(x) for x in input().split()]

    print(*sortAbs(line))

if __name__ == "__main__":
    main()
