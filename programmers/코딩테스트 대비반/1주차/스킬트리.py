def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        skill_set = list(skill)
        flag = True 
        for i in tree: 
            if i in skill_set:
                if (i == skill_set[0]): 
                    skill_set.pop(0)
                else:
                    flag = False 
                    break
            else: 
                continue 
                
        if flag == True: 
            answer += 1 

    return answer
