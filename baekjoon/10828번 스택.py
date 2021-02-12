import sys
mystack = []
N = int(input())
input = sys.stdin.readline
for _ in range(N):
    m = list(map(str,input().split()))   
    if m[0] == 'push':
        mystack.append(int(m[1]))
    elif m[0] == 'pop':
        if len(mystack) == 0:
            print(-1)
        else:
            print(mystack.pop())
    elif m[0] == 'size':
        print(len(mystack))
    elif m[0] == 'empty':
        if len(mystack) == 0: 
            print(1)
        else:
            print(0)
    elif m[0] == 'top':
        if len(mystack) == 0: 
            print(-1)
        else:
            print(mystack[-1])
