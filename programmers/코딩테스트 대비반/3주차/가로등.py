'''
아래의 두가지 방식으로 하면 런타임 에러
- 양 끝의 경우 가장 값이 작고, 큰 가로등만 비교하면 되는데 전체를 비교한 후 테스트 
'''
# 완전 탐색
def solution(l, v):
    for i in range(1, 1000000000): 
        # 0.5 단위로 계산하려고 (l+1)*2를 계산 
        s = [0] * (2*i) + [1 for _ in range(0, l*2+1, 1)] + [0] * (2*i)
        for j in v: 
            s[2*i+2*j-(2*i) : 2*i+2*j+(2*i)+1:] = [0] * ((2*i + 2*j+(2*i)) - (2*i + 2*j-(2*i)) + 1)

        if sum(s) == 0: 
            return i
    return -1

# 이진 탐색
def solution(l, v):
    lower = 1
    upper = l 
    while lower <= upper: 
        i = (lower + upper)//2
        # 0.5 단위로 계산하려고 (l+1)*2를 계산 
        s = [0] * (2*i) + [1 for _ in range(0, l*2+1, 1)] + [0] * (2*i)
        for j in v: 
            s[2*i+2*j-(2*i) : 2*i+2*j+(2*i)+1:] = [0] * ((2*i + 2*j+(2*i)) - (2*i + 2*j-(2*i)) + 1)

        if sum(s) == 0: 
            upper = i - 1 # 최대값 나추기
        else:
            lower = i + 1 # 최소값 높이기 
    return upper + 1

'''
양 끝을 먼저 비교하고 남은 가로등을 비교하도록 수정
출처 : https://huidea.tistory.com/123
'''
def is_possible(road_length, locations, light_range):

	# 양 끝의 경우 다 채워지는지 확인 
    if 0 < locations[0] - light_range or locations[-1] + light_range < road_length:
        return False
    
    # 사이사이 가로등 채워지는지 확인
    for i in range(1, len(locations)):
        if locations[i-1] + light_range < locations[i] - light_range:
            return False
            
    # 다 통과하면 해당 범위 가능 
    return True


def solution(road_length, locations):
    locations.sort()

    lower = 1
    upper = road_length
    while lower <= upper:
        mid = (lower + upper) // 2
        
        ### 해당 범위가 가능하더라도 최소값을 찾기 때문에 ***
        if is_possible(road_length, locations, mid): 
            upper = mid - 1 # 최대값 나추기
        else:
            lower = mid + 1 # 최소값 올리기
    return upper + 1
