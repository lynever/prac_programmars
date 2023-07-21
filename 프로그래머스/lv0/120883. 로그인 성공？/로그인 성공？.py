def solution(id_pw, db):
    answer = 'fail'
    for iden, pw in db:
        if id_pw[0] == iden:
            answer = 'login' if id_pw[1] == pw else 'wrong pw'
    return answer