def getSmallEquElements (array, pivot) :
    '''
    array에서 pivot보다 작거나 같은 원소들을 list로 반환하는 함수
    '''
    
    result = []
    
    for x in array :
        if pivot >= x :
            result.append(x)
    
    return result
    

def getLargeElements (array, pivot) :
    '''
    array에서 pivot보다 큰 원소들을 list로 반환하는 함수
    '''
    
    result = []
    
    for x in array :
        if x > pivot :
            result.append(x)
    
    return result
    

def quickSort(array):
    '''
    퀵정렬을 통해 오름차순으로 정렬된 array를반환하는 함수를 작성하세요.
    '''

    '''
    1. pivot 을 잡는다 : array[0]
    2. pivot 보다 작거나 같은 친구를 left 에다가 대입한다
    3. pivot 보다 큰 친구를 right 에다가 대입한다.
    4. left, right 를 각각 정렬한다.
    5. left + pivot + right 를 반환한다.
    '''
    
    if len(array) <= 1 :
        return array
    
    pivot = array[0]
    
    left = getSmallEquElements(array[1:], pivot) # 작거나 같은 element들 
    right = getLargeElements(array[1:], pivot)
    
    left = quickSort(left)
    right = quickSort(right)
    
    # left 와 right를 정렬 완료
    
    return left + [pivot] + right

def main():
    line = [int(x) for x in input().split()]

    print(*quickSort(line))

if __name__ == "__main__":
    main()


