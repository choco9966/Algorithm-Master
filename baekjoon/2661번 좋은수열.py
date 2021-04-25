# 출처 : https://sungmin-joo.tistory.com/66 [Big-Joo의 공부기록]
# 백트래킹 
def solve(idx):
    for i in range(1, (idx//2)+1):
        if s[-i:] == s[-2*i:-i]: return -1 
    
    if idx == n: 
        for i in range(n): 
            print(s[i], end = '') 
        return 0

    for i in range(1, 4): 
        s.append(i) 
        if solve(idx + 1) == 0: 
            return 0
        s.pop()

if __name__ == "__main__": 
    n = int(input())
    s = [] 
    solve(0)
