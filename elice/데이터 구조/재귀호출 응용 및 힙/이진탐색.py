def binarySearch(array, value):
    '''
    array에 value가 존재하면 True를, 존재하지 않으면 False를 반환합니다.
    '''
    m = len(array)//2
    if len(array) == 1 :
        if array[0] == value:
            return True
        else :
            return False
    if array[m] == value :
        return True
    if array[m] < value :
        return binarySearch(array[m:],value)
    if array[m] > value :
        return binarySearch(array[:m],value)


def main():
    '''
    Do not change this code
    '''
    array_len = int(input())
    array = [int(x) for x in input().strip().split(" ")]
    target = int(input())
    print(binarySearch(array, target))

if __name__ == "__main__":
    main()
