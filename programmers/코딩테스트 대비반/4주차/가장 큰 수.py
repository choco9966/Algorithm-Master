def solution(numbers):
    '''
    곱하기 5를 해준경우와 그렇지 않은 경우의 정렬순서 
    ['99999', '55555', '3434343434', '33333', '3030303030']
    ['9', '5', '34', '30', '3']
    '''
    numbers = sorted(map(str, numbers), key=lambda x: x*5, reverse=True)
    # int -> str : 맨 앞자리가 0이 올 수도 있음 (테스트11) [0,0,0,0,0]
    return str(int(''.join(numbers)))
