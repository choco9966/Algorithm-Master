import sys
sys.setrecursionlimit(100000)

def paper(myMap,s_i,e_i,s_j,e_j) :
    flag = True
    num = myMap[s_i][s_j]
    for i in range(s_i,e_i+1) :
        for j in range(s_j,e_j+1) :
            if num != myMap[i][j] :
                flag = False
                break
        if not flag :
            break
    if flag :
        if num :
            return (0,1)
        else :
            return (1,0)
    whiteCnt = 0
    blueCnt = 0
    result = (whiteCnt,blueCnt)
    result = tuple(sum(x) for x in zip(result,paper(myMap,s_i,(s_i+e_i)//2,s_j,(s_j+e_j)//2)))
    result = tuple(sum(x) for x in zip(result,paper(myMap,(s_i+e_i)//2+1,e_i,s_j,(s_j+e_j)//2)))
    result = tuple(sum(x) for x in zip(result,paper(myMap,s_i,(s_i+e_i)//2,(s_j+e_j)//2+1,e_j)))
    result = tuple(sum(x) for x in zip(result,paper(myMap,(s_i+e_i)//2+1,e_i,(s_j+e_j)//2+1,e_j)))
    
    return result

def getPaperCount(myMap) :
    '''
    n x n 의 색종이가 주어질 때, 하얀색 색종이의 개수와 파란색 색종이의 개수를 tuple로 반환하는 함수를 작성하세요.
    '''
    
    
    return paper(myMap,0,len(myMap)-1,0,len(myMap)-1)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    myMap = []
    for i in range(n) :
        myMap.append([int(x) for x in input().split()])

    print(getPaperCount(myMap))

if __name__ == "__main__":
    main()
