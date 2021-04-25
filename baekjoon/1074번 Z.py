# 참고자료 : https://deok2kim.tistory.com/74
## 분할정복을 이용한 풀이 
## 핵심 : 시간초과를 방지하기 위해서 해당 좌표가 들어있는 박스만 탐색해야함 
## 틀린점 : 위의 코드와 동일한 방식으로 접근했는데 else부분의 x와 y좌표가 들어가는 부분을 row와 col으로 비교해야하는데 이 부분에서 실수를 했음 
N, r, c = map(int, input().split())
def check_size(row1, col1, row2, col2): 
    return True if row1 <= r < row2 and col1 <= c < col2 else False

def check_result(row, col): 
    return True if row == r and col == c else False

def Z(row, col, size, num):
    if size == 2: 
        if check_result(row, col): 
            print(num)
            return 
        num += 1

        if check_result(row, col+1): 
            print(num)
            return 
        num += 1

        if check_result(row+1, col): 
            print(num)
            return 
        num += 1

        if check_result(row+1, col+1): 
            print(num)
            return 
        num += 1

    else: 
        half_size = size // 2 
        if check_size(row, col, row+half_size, col+half_size): 
            Z(row, col, half_size, num)
        elif check_size(row, col+half_size, row+half_size, col+size): 
            Z(row, col+half_size, half_size, num+(half_size**2)*1)
        elif check_size(row+half_size, col, row+half_size*2, col+half_size): 
            Z(row+half_size, col, half_size, num+(half_size**2)*2)
        else: 
            Z(row+half_size, col+half_size, half_size, num+(half_size**2)*3)

Z(0, 0, 2**N, 0)
