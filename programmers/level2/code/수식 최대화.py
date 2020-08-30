from itertools import permutations
import re 

def is_number(n):
    is_number = True
    try:
        num = float(n)
        # check for "nan" floats
        is_number = num == num   # or use `math.isnan(num)`
    except ValueError:
        is_number = False
    return is_number
    
def solution(expression):
    num = re.findall('\d+', expression)
    other = re.findall('\D', expression)
    answer = []

    for i in list(permutations(set(other), len(set(other)))):
        cal = [num[0]]
        num_stack = []
        other_stack = []
        x = '/'

        for j in range(len(other)):
            cal.append(other[j])
            cal.append(num[j+1])

        for k in i:
            while (x != k) & (len(cal) >= 1): 
                x = cal.pop()
                if x == k: 
                    x = int(cal.pop())
                    if k == '-':
                        try:
                            if cal[-1] == '-':
                                cal.append(x + num_stack.pop())
                            else:
                                cal.append(x - num_stack.pop())
                        except:
                            cal.append(x - num_stack.pop())
                    elif k == '+':
                        cal.append(x + num_stack.pop())
                    else:
                        cal.append(x * num_stack.pop())
                else:
                    if is_number(str(x)) == True: num_stack.append(int(x))
                    else: other_stack.append(x)

            cal.append(str(num_stack.pop()))

            for i in range(len(other_stack)):
                cal.append(str(other_stack.pop()))
                cal.append(str(num_stack.pop()))
        answer.append(abs(int(cal.pop())))
    return max(answer)
