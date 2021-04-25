import sys

def attending(meetingList) :
    '''
    회의 일정이 list로 주어질 때, 엘리스씨가 참석할 수 있는 최대 회의 수를 반환하는 함수를 작성하세요. 
    '''

    meetingList = sorted(meetingList, key=lambda x: x[1])
    result = 1
    end = meetingList[0][1]

    n = len(meetingList)

    for i in range(1, n) :
        if end <= meetingList[i][0] :
            result += 1
            end = meetingList[i][1]

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    meetingList = []

    for i in range(n) :
        data = [int(x) for x in input().split()]
        meetingList.append( (data[0], data[1]) )

    print(attending(meetingList))

if __name__ == "__main__":
    main()
