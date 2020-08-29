def solution(priorities, location):
    answer = 0

    array1 = [c for c in range(len(priorities))] # index 위치 저장 
    array2 = priorities.copy() # 값 저장 (출력되는 값)

    i = 0
    while True:
        if array2[i] < max(array2[i+1:]):
            array1.append(array1.pop(i))
            array2.append(array2.pop(i))
        else:
            i += 1

        if array2 == sorted(array2, reverse=True):
            break

    return array1.index(location) + 1
