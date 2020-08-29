# ord를 이용해서 알파벳의 위치를 출력하고 순차적으로 진행하는게 빠른지, 반대로 진행하는게 빠른 지 계산 
def cal_change_alphabet(solution):
    diff = min(abs(ord(solution)-ord('A')), abs(26 - (ord(solution)-ord('A'))))
    return diff

def change_alphabet(text, index):
    text_ = list(text)
    text_[index] = 'A'
    text = ''.join(text_)
    return text

def check_alphabet(text):
    if len(set(list(text))) == 1: 
        return True

def solution(name):
    answer_list = []
    answer = 0
    n = len(name)

    # 알파벳을 모두 A로 바꿨을 때 갯수 
    for i in range(n):
        answer += cal_change_alphabet(name[i])

    name = change_alphabet(name, 0)

    if check_alphabet(name) == 1: return 0

    # 조작키를 이용해서 이동하는 최소의 갯수 
    # 1. 오른쪽으로 갔다가 왼쪽으로 가는 경우 
    for i in range(1, n):
        name_left = name
        answer_left = answer + i
        for k in range(1, i+1):
            name_left = change_alphabet(name_left, k)

        for j in range(1, n-i):
            name_left = change_alphabet(name_left, i-j)
            answer_left += 1
            if check_alphabet(name_left): break
        answer_list.append(answer_left)

    # 2. 왼쪽으로 갔다가 오른쪽으로 가는 경우 
    for i in range(1, n):
        name_right = name
        answer_right = answer + i
        for k in range(1, i+1):
            name_right = change_alphabet(name_right, -k)

        for j in range(0, n-i):
            name_right = change_alphabet(name_right, -i+j)
            if check_alphabet(name_right): break
            answer_right += 1

        answer_list.append(answer_right)

    return min(answer_list)
