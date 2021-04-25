import sys
sys.setrecursionlimit(100000)

def strContain(A, B) :
    '''
    문자열 A의 알파벳이 문자열 B에 모두 포함되어 있으면 "Yes", 아니면 "No"를 반환합니다.
    '''

    if len(A) <= 0 :
        return "Yes"

    if A[0] in B :
        return strContain(A[1:], B)
    else :
        return "No"

def main():
    '''
    Do not change this code
    '''

    A = input()
    B = input()

    print(strContain(A, B))

if __name__ == "__main__":
    main()
