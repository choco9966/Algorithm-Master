# 참고자료 : https://deok2kim.tistory.com/74
## 분할정복을 이용한 풀이 
## 핵심 : 시간초과를 방지하기 위해서 해당 좌표가 들어있는 박스만 탐색해야함 
## 틀린점 : 위의 코드와 동일한 방식으로 접근했는데 else부분의 x와 y좌표가 들어가는 부분을 row와 col으로 비교해야하는데 이 부분에서 실수를 했음 
def Z(row, col, size, num): # (row,col: 자른 box의 첫번째 인덱스, size: box 사이즈, num: box 시작점의 숫자)
    if size == 2: # 사이즈가 2x2가 됐을 때
        if row == r and col == c:
            print(num)
            return
        num += 1

        if row == r and col + 1 == c:
            print(num)
            return
        num += 1

        if row + 1 == r and col == c:
            print(num)
            return
        num += 1

        if row + 1 == r and col + 1 == c:
            print(num)
            return
        num += 1

    else:
        half_size = size // 2
        # 왼쪽 위
        if row <= r < row + half_size and col <= c < col + half_size:
            Z(row, col, half_size, num)
        # 오른쪽 위
        elif row <= r < row + half_size and col + half_size <= c < col + size:
            Z(row, col + half_size, half_size, num + (half_size ** 2) * 1)
        # 왼쪽 아래
        elif row + half_size <= r < row + half_size * 2 and col <= c < col + half_size:
            Z(row + half_size, col, half_size, num + (half_size ** 2) * 2)
        # 오른쪽 아래
        elif row + half_size <= r < row + half_size * 2 and col + half_size <= c < col + size:
            Z(row + half_size, col + half_size, half_size, num + (half_size ** 2) * 3)


if __name__ == "__main__":
    N, r, c = map(int, input().split())
    Z(0, 0, 2 ** N, 0)
