def solution(s):
    answer = True
    Queue = []
    for i in s: 
        if i == '(': Queue.append('(')
        else: 
            try: Queue.pop() 
            except: return False
    if len(Queue) == 0: return True
    else: return False
