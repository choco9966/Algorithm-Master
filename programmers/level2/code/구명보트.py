def solution(people, limit):
    people = sorted(people)
    answer = 0
    start_index = 0
    last_index = len(people) - 1

    while start_index <= last_index: 
        A = people[last_index]
        answer += 1
        boat = A
        while start_index <= last_index:
            # 보트에 무게가 늘어나는 것을 반영해야 함 
            if people[start_index] + boat <= limit: boat += people[start_index]; start_index += 1
            else: break
        last_index -= 1
    return answer
