from collections import deque, Counter
def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    if len(participant) == len(completion):
        for i, j in participant.items(): 
            if completion[i] != j: 
                return i
    else:
        return list(set(list(participant.keys())).difference(set(list(completion.keys()))))[0]


from collections import Counter

def solution(participant, completion):
    return list((Counter(participant) - Counter(completion)).keys())[0]
