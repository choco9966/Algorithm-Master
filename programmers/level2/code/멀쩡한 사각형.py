def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y) 

def solution(w,h):
    return w*h - (w+h-gcd(w, h))
