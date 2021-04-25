import sys 
input = sys.stdin.readline
def gcd(x, y): 
    if x % y == 0: 
        return y
    else:
        return gcd(y, x % y)

def howManyTree(n, myInput) :
    '''
    모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 리턴하는 함수를 구현하세요.
    '''
    diff = []
    myInput = sorted(myInput)
    for i in range(n-1):
        diff.append(myInput[i+1] - myInput[i])

    GCD = gcd(diff[0], diff[1])
    diff = diff[2:]
    for i in range(len(diff)):
        GCD = gcd(GCD, diff[i])

    cnt =  (max(myInput) - min(myInput)) / GCD - len(myInput) + 1
    return int(cnt)

def main():
    n = int(input())
    myInput = []
    for _ in range(n) :
        myInput.append(int(input()))
    print(howManyTree(n, myInput))

if __name__ == "__main__":
    main()
