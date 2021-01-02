from collections import Counter
from itertools import combinations 
def solution(m, weights):
    answer = 0
    for i in range(1, len(weights)):
        answer += Counter(map(sum, combinations(weights, i)))[m]
        if sorted(Counter(map(sum, combinations(weights, i))).keys())[0] > m: 
            return answer
    return answer
