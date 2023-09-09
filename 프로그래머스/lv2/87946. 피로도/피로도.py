from itertools import permutations
def solution(k, dungeons):
    perm = list(permutations(dungeons, len(dungeons)))
    anslst = []
    for i in perm:
        answer, tmp = 0, k
        for minp, usep in i:
            if tmp >= minp:
                tmp -= usep
                answer += 1
        if answer == len(dungeons):
            break
        else:
            anslst.append(answer)
    return answer if answer == len(dungeons) else max(anslst)