import sys

def fKnapsack(materials, m) :
    '''
    크기 m까지 버틸 수 있는 베낭이 담을 수 있는 최대 가치를 반환하는 함수를 작성하세요.

    주의 : 셋째 자리에서 반올림하는 것을 고려하지 않고 작성하셔도 됩니다. 
    '''

    values = []
    result = 0

    for mat in materials :
        values.append( (mat[0], mat[1], mat[1] / mat[0]) )

    values = sorted(values, key=lambda x: x[2], reverse=True)

    for v in values :
        if m >= v[0] :
            result += v[1]
            m -= v[0]
        else :
            result += (v[1] / v[0]) * m
            break

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    line = [int(x) for x in input().split()]

    n = line[0]
    m = line[1]

    materials = []

    for i in range(n) :
        data = [int(x) for x in input().split()]
        materials.append( (data[0], data[1]) )

    print("%.3lf" % fKnapsack(materials, m))

if __name__ == "__main__":
    main()
