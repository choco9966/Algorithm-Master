from itertools import permutations
def findcase(answer, num, strike, ball):
    answer_list = []
    if strike == 3:
        return [str(num)]
    else:
        if strike == 2:
            # ball이 있는게 불가능함 
            for i in answer:
                # 앞 2개가 같은 경우 
                if (i[0] == str(num)[0]) & (i[1] == str(num)[1]) & (i[2] != str(num)[2]): 
                    answer_list.append(i)
                # 앞, 뒤가 같은 경우 
                elif (i[0] == str(num)[0]) & (i[2] == str(num)[2]) & (i[1] != str(num)[1]): 
                    answer_list.append(i)            
                # 뒤 2개가 같은 경우 
                elif (i[1] == str(num)[1]) & (i[2] == str(num)[2]) & (i[0] != str(num)[0]): 
                    answer_list.append(i)

        elif strike == 1: 
            for i in answer:
                # 앞 1개가 같은 경우 
                if (i[0] == str(num)[0]) & (i[1] != str(num)[1]) & (i[2] != str(num)[2]): 
                    # ball이 2개인 경우 
                    if (ball == 2) & (i[1] == str(num)[2]) & (i[2] == str(num)[1]):
                        answer_list.append(i)
                    # ball이 1개인 경우 
                    elif (ball == 1) & ((i[1] == str(num)[2]) | (i[2] == str(num)[1])):
                        print(str(num). i)
                        answer_list.append(i)
                    # ball이 0개인 경우 
                    elif (ball == 0) & (i[1] != str(num)[2]) & (i[2] != str(num)[1]):
                        answer_list.append(i)
                # 중간 1개가 같은 경우 
                elif (i[1] == str(num)[1]) & (i[0] != str(num)[0]) & (i[2] != str(num)[2]): 
                    # ball이 2개인 경우 
                    if (ball == 2) & (i[0] == str(num)[2]) & (i[2] == str(num)[0]):
                        answer_list.append(i)
                    # ball이 1개인 경우 
                    elif (ball == 1) & ((i[0] == str(num)[2]) | (i[2] == str(num)[0])): 
                        answer_list.append(i)
                    # ball이 0개인 경우 
                    elif (ball == 0) & (i[0] != str(num)[2]) & (i[2] != str(num)[0]):
                        answer_list.append(i)
                # 끝 1개가 같은 경우 
                elif (i[2] == str(num)[2]) & (i[1] != str(num)[1]) & (i[0] != str(num)[0]): 
                    # ball이 2개인 경우 
                    if (ball == 2) & (i[0] == str(num)[1]) & (i[1] == str(num)[0]):
                        answer_list.append(i)
                    # ball이 1개인 경우 
                    elif (ball == 1) & ((i[0] == str(num)[1]) | (i[1] == str(num)[0])): 
                        answer_list.append(i)
                    # ball이 0개인 경우 
                    elif (ball == 0) & (i[0] != str(num)[1]) & (i[1] != str(num)[0]):
                        answer_list.append(i)
                    else:
                        pass 
        else:
            for i in answer:
                if ((i)[0] != str(num)[0]) & ((i)[1] != str(num)[1]) & ((i)[2] != str(num)[2]): 
                    # ball이 3개인 경우 
                    if (ball == 3) & ((i)[0] in list(str(num))) & ((i)[1] in list(str(num))) & ((i)[2] in list(str(num))): answer_list.append(i)
                    # ball이 2개인 경우 
                    elif (ball == 2) & ((i)[0] in list(str(num))) & (((i)[1] in list(str(num))) | ((i)[2] in list(str(num)))): answer_list.append(i)
                    elif (ball == 2) & ((i)[1] in list(str(num))) & (((i)[2] in list(str(num))) | ((i)[0] in list(str(num)))): answer_list.append(i)
                    elif (ball == 2) & ((i)[2] in list(str(num))) & (((i)[0] in list(str(num))) | ((i)[1] in list(str(num)))): answer_list.append(i)
                    # ball이 1개인 경우
                    elif (ball == 1) & ((i)[0] in list(str(num))) & ((i)[1] not in list(str(num))) & ((i)[2] not in list(str(num))): answer_list.append(i)
                    elif (ball == 1) & ((i)[1] in list(str(num))) & ((i)[2] not in list(str(num))) & ((i)[0] not in list(str(num))): answer_list.append(i)
                    elif (ball == 1) & ((i)[2] in list(str(num))) & ((i)[0] not in list(str(num))) & ((i)[1] not in list(str(num))): answer_list.append(i)
                    # ball이 0개인 경우 
                    elif (ball == 0) & ((i)[0] not in list(str(num))) & ((i)[1] not in list(str(num))) & ((i)[2] not in list(str(num))): answer_list.append(i)
    return answer_list



def solution(baseball):
    # 모든 경우의 수 
    answer = list(map(''.join, permutations([str(i) for i in range(1, 10)], 3)))
    # 스트라이크, 볼순으로 정렬 
    baseball = sorted(baseball, key = lambda x: (-x[1], -x[2]))
    # print(baseball)
    while len(baseball) > 0 :
        if len(answer) == 1: 
            return 1
        A = baseball.pop(0)
        # 해당하는 경우의 수를 찾아주기 
        answer = findcase(answer, A[0], A[1], A[2])
        # print(answer)
    # print(answer)
    return len(answer)
