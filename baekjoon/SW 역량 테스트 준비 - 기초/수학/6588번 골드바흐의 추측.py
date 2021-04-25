import math, sys
a = [0, 0] + [1]*(2*1000000-1) # 0과 1은 제외 
for i in range(2, int(math.sqrt(1000000))+1): 
    for j in range(2*i, 1000000+1, i): 
        a[j] = 0

while True: 
    N = int(sys.stdin.readline())
    if N == 0: 
        break
    flag = False 
    for i in range(3, 1000000, 2): 
        if a[i] == 1 and a[N - i] == 1: 
            flag = True 
            print(N, '=', i, '+', N-i)
            break 
    if flag == False: 
        print("Goldbach's conjecture is wrong.")