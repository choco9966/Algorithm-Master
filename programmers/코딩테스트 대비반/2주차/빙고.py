def solution(board, nums):
    '''
    정답은 맞았으나 시간초과 발생 
    '''
    cnt = 0
    boards = [[0] * len(board[0]) for _ in range(len(board))]
    for i, row in enumerate(board): 
        for j, v in enumerate(row): 
            if v in nums: 
                boards[i][j] = 1
    
    # 행이 빙고인 경우 
    for row in boards: 
        if sum(row) == len(board[0]):
            cnt += 1
    
    # 열이 빙고인 경우 
    for row in list(zip(*boards)): 
        if sum(row) == len(board[0]):
            cnt += 1    
            
    # 대각선이 빙고인 경우 
    x = []
    for i in range(len(boards)):
        if boards[i][i] == 1: 
            continue 
        else:
            cnt -= 1
            break 
    cnt += 1
    
    x = []
    for i in range(len(boards)):
        if boards[len(boards[0])-i-1][i] == 1: 
            continue 
        else:
            cnt -= 1
            break
    cnt += 1
        
    return cnt 


def solution(board, nums):
    '''
    다른사람 풀이
    출처 : https://velog.io/@rapsby/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B9%99%EA%B3%A0-python
    '''
    n = len(board)
    nums = dict.fromkeys(nums)
    row_list = [0] * n
    col_list = [0] * n
    line1 = 0
    line2 = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] in nums:
                board[i][j] = 0
                row_list[i] += 1
                col_list[j] += 1
                if i == j:
                    line1 += 1
                if n - 1 - i == j:
                    line2 += 1
    answer = line1//n + line2//n
    answer += sum([1 for i in row_list if i == n])
    answer += sum([1 for i in col_list if i == n])
    return answer
