'''
# 강사님 코드 
def binarySearch(array, value):
    '''
    array에 value가 존재하면 True를, 존재하지 않으면 False를 반환합니다.
    참고로, 해당 코드는 입력값이 오름차순으로 정렬되었다는것을 가정으로 하고 실행되어지는 코드임
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
'''
def binarySearch(array, value):
    '''
    array에 value가 존재하면 True를, 존재하지 않으면 False를 반환합니다.
    '''
    
    if len(array) != 0:  
        left_array = array[0:len(array)//2]
        center = array[len(array)//2]
        right_array = array[len(array)//2+1:]
        if center == value: 
            return True 
        else: 
            flag = False 
            flag = binarySearch(left_array, value)
            if flag == False:
                flag = binarySearch(right_array, value)
            return flag  
    else:
        return False 


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
