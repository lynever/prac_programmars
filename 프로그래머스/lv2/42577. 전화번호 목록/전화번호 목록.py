def solution(phone_book):
    answer = True
    phone_book.sort()
    for idx, val in enumerate(phone_book):
        if idx != len(phone_book) - 1 and val == phone_book[idx + 1][:len(val)]:
            answer = False
            break
    return answer