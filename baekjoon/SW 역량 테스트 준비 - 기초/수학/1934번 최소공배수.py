import sys
def GCD(x, y) :
    if y == 0 :
        return x
    else :
        return GCD(y, x%y)

for _ in range(int(input())):
    n1, n2 = map(int, input().split())
    gcd = GCD(n1, n2)
    print(gcd * (n1//gcd) * (n2//gcd))