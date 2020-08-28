def solution(record):
    answer = []
    userdict = {}
    # mes : record의 message 
    # message를 받음과 동시에 유저 아이디 : 닉네임을 저장 
    # Enter, Change가 들어온 경우 dictionary에 저장
    for mes in record: 
        if (mes.split(' ')[0] == 'Enter') | (mes.split(' ')[0] == 'Change'):
            userdict[mes.split(' ')[1]] = mes.split(' ')[2]

    # for문을 돌면서, 하나씩 출력 
    for mes in record: 
        if mes.split(' ')[0] == 'Enter': 
            # userdict[mes.split(' ')[1]] + '님이 들어왔습니다.' 이런식으로 해도 가능 
            answer.append("{}님이 들어왔습니다.".format(userdict[mes.split(' ')[1]]))
        elif mes.split(' ')[0] == 'Leave': 
            answer.append("{}님이 나갔습니다.".format(userdict[mes.split(' ')[1]]))
        else:
            pass
    return answer