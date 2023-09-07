def solution(citations):
    citations.sort()
    answer = citations[-1]
    while answer > 0:
        mnval, mxval = 0, 0
        for i in citations:
            if i >= answer:
                mxval += 1
            else:
                mnval += 1
        if mnval <= answer <= mxval:
            break
        else:
            answer -= 1
    return answer