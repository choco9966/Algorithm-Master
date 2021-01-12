def findKth(myInput, k) :
    '''
    매 순간마다 k번째로 작은 원소를 리스트로 반환합니다.
    
    myInput = [1, 8, 3, 4, 2, 5, 3, 6, 4, 3]
    k
    '''

    data = []
    result = []
    
    for element in myInput :
        data.append(element)
        
        data.sort()
        
        if len(data) < k :
            result.append(-1)
        else :
            result.append(data[k-1])

    return result

def main():
    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    firstLine = [int(x) for x in input().split()]
    myInput = [int(x) for x in input().split()]

    print(*findKth(myInput, firstLine[1]))
if __name__ == "__main__":
    main()


