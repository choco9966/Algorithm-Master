import sys

def search(data,s,e,key):
    if s==e :
        if data[s] == key :
            return "Yes"
        else :
            return "No"
    if data[(s+e)//2] > key :
        return search(data,s,(s+e)//2,key)
    elif data[(s+e)//2] < key :
        return search(data,(s+e)//2+1,e,key)
    else :
        return "Yes"

def binarySearch(data, m) :
    '''
    n개의 숫자 중에서 m이 존재하면 "Yes", 존재하지 않으면 "No"를 반환하는 함수를 작성하세요.
    '''
    
    return search(data,0,len(data)-1,m)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]
    m = int(input())

    print(binarySearch(data, m))

if __name__ == "__main__":
    main()
