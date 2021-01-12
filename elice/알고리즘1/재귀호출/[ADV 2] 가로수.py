def gcd(n,m) :
    while m!=0 :
        n,m = m,n%m
    return n

def howManyTree(n, myInput) :
    '''
    모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 리턴하는 함수를 구현하세요.
    '''
    
    diff = []
    cnt = 0

    myInput.sort()

    for i in range(1,len(myInput)) :
        diff.append(myInput[i] - myInput[i-1])

    diff.sort()
    
    GCD = diff[0]

    for x in diff :
        GCD = gcd(GCD,x)
    for x in diff :
        cnt += x//GCD-1

    return cnt

def main():
    '''
    수정하시면 안됩니다.
    '''
    n = int(input())
    myInput = []
    for _ in range(n) :
        myInput.append(int(input()))

    print(howManyTree(n, myInput))
if __name__ == "__main__":
    main()
