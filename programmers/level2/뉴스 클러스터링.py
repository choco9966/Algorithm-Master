from collections import Counter 

# https://eda-ai-lab.tistory.com/501
def solution(str1, str2):
    answer = 0

    # 1. str1의 값을 2칸단위로 쪼갬
    # 2. 두값이 모두 알파벳이면 소문자로 바꿔서 list1에 저장 
    list1 = []
    for i in range(0, len(str1)-1): 
        if str1[i:i+2].isalpha(): list1.append(str1[i:i+2].lower())

    # 위의 str1에 했던 작업을  str2에 동일하게 적용 
    list2 = []
    for i in range(0, len(str2)-1): 
        if str2[i:i+2].isalpha(): list2.append(str2[i:i+2].lower())

    # 다중집합이 아닌 경우에는 교집합 / 합집합으로 계산 
    # 단, 분모가 0이어서 try가 실패하는 경우에는 65536 출력 
    if (len(list1) == len(set(list1))) & (len(list2) == len(set(list2))): 
        try: 
            answer = len(set(list1).intersection(set(list2))) / (len(set(list1).union(set(list2))))
            return int(answer * 65536)
        except: 
            return 65536
    # 다중집합의 경우 
    # 1. list1의 원소와 list2의 원소에 대해서 Counter를 계산 
    # 2. 계산한 Counter의 key를 전부 참조하면서 긴 값은 union에 짧은 값은 intersection에 저장 
    # 단, 둘 중 하나에만 있는 경우는 union에만 저장 (except 부분) 
    # 위와 마찬가지로 분모가 0인 경우에는 65536 출력 
    else: 
        union = 0
        inter = 0
        clist1 = Counter(list1)
        clist2 = Counter(list2)
        for i in set(list(clist1.keys()) + list(clist2.keys())): 
            # 다중집합에서도 두개의 집합에만 포함되는 경우는 긴쪽은 union, 짧은 쪽은 inter에 저장 
            try: 
                # 긴 값을 찾아서 긴 값을 union, 짧은 값을 inter에 저장 
                if clist1[i] > clist2[i]: 
                    union += clist1[i]
                    inter += clist2[i]
                else: 
                    inter += clist1[i]
                    union += clist2[i]
               # 다중집합에서도 하나의 집합에만 포함되는 경우는 union에만 저장 
            except: 
                if i in list1: union += clist1[i]
                else : union += clist2[i]
        try:      
            answer = inter / (union)
            return int(answer * 65536)
        except:
            return 65536