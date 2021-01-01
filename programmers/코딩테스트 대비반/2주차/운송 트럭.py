def solution(max_weight, specs, names):
    answer = 0
    weight = 0
    dict_specs = dict(specs)
    
    for name in names:
        weight += int(dict_specs.get(name))
        if weight > max_weight:
            answer += 1
            weight = int(dict_specs.get(name))
    
    if weight != 0:
        answer += 1
    
    return answer
