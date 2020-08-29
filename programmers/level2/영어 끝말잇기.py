def solution(n, words):
    answer = [0, 0]
    count = 1 # range가 1부터 시작하므로, 1으로 설정 
    for idx in range(1, len(words)): # 1부터 시작하는 이유는 첫번째 사람의 첫 단어는 절대 틀릴 일이 없음 
        word = words[idx] # words[idx] : 언급된 단어 
        count %= n 
        if (word in words[0:idx]) or (words[idx-1][-1] != word[0]): 
            answer = [count +1, 1 + idx//n]
            return answer 
        count +=1 
    return answer
