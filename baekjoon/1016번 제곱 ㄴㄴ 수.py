# 출처 : https://nerogarret.tistory.com/32
import sys, math

results = []
min_num, max_num = map(int, sys.stdin.readline().split())
validation = [1 for _ in range(min_num, max_num+1)]

search_target = int(math.sqrt(max_num))
# max의 값보다 작은 모든 제곱수의 목록을 생성
squares = [v**2 for v in range(2, search_target+1)]
for square in squares:
    # min부터 max까지의 수 중, 해당 제곱수의 최소의 배수를 구함.
    cur_idx = (math.ceil(min_num / square) * square) - min_num
    while cur_idx <= max_num - min_num:
        # 제곱수의 배수인 경우 0으로 대체
        validation[cur_idx] = 0
        # 다음 제곱수의 index를 구함.
        cur_idx += square

# 남은 1들의 개수가 제곱 ㄴㄴ수의 개수가 된다.
result = sum(validation)
results.append(result)

for result in results:
    sys.stdout.write(str(result))
