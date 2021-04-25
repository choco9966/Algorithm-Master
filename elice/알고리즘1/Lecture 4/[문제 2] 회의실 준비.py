import sys

def reservation(meetingList) :
    '''
    회의 일정이 list로 주어질 때, 엘리스씨가 준비해야 하는 회의실의 수의 최솟값을 반환하는 함수를 작성하세요.

    각 일정은 tuple로 주어진다. 예를 들어, 주어진 입력의 경우 다음과 같이 저장된다.
    
    meetingList[0] = (1, 4)
    meetingList[1] = (3, 5)
    meetingList[2] = (2, 7)
    meetingList[3] = (4, 6)
    '''
    
    meetingList.sort()
    endTime = []
    result = 0

    '''
    meetingList = [(1,4),(2,7),(3,5),(4,6)]
    i) m = (1,4)
        tempQueue = []
        endTime = [4]
        result = 1
    ii) m = (2,7)
        tempQueue = [4]
        endTime = [4,7]
        result = 2
    iii) m = (3,5)
        tempQueue = [4,7]
        endTime = [4,7,5]
        result = 3
    iv) m = (4,6)
        tempQueue = [5,7]
        endTime = [5,7,6]
        result = 3
    '''

    for m in meetingList :
        tempQueue = []

        for e in endTime :
            if e > m[0] :
                tempQueue.append(e)

        endTime = list(tempQueue)
        endTime.append(m[1])

        result = max(result, len(endTime))

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

    print(reservation(meetingList))

if __name__ == "__main__":
    main()
