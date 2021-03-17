import sys
N = int(input())
RGB = list(map(int, sys.stdin.readline().split()))
for i in range(N-1): 
    r, g, b = map(int, sys.stdin.readline().split())
    # 하나의 줄로 계산을 안하면 바뀐 값의 RGB가 영향을 줌 
    RGB[0], RGB[1], RGB[2] = min(RGB[1]+r, RGB[2]+r), min(RGB[0]+g, RGB[2]+g), min(RGB[0]+b, RGB[1]+b)
print(min(RGB))
