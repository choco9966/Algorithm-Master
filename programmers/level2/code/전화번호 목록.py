def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    while len(phone_book) > 1: 
        start = 0
        A = phone_book.pop(0)
        while (phone_book[start][0] == A[0]) & (start < len(phone_book)):
            if A == phone_book[start][0:len(A)]:
                answer = False
                break
            start += 1
            if answer == False: break
    return answer
