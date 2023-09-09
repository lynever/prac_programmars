def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    partiallst1, partiallst2 = [], []
    for idx, val in enumerate(str1):
        if idx != len(str1) - 1 and (val + str1[idx + 1]).isalpha():
            partiallst1.append(val + str1[idx + 1])
    for idx2, val2 in enumerate(str2):
        if idx2 != len(str2) - 1 and (val2 + str2[idx2 + 1]).isalpha():
            partiallst2.append(val2 + str2[idx2 + 1])
    multiset1, multiset2 = [], []
    for i in partiallst1:
        n = partiallst1.count(i)
        for j in range(n):
            multiset1.append((i, j))
    for k in partiallst2:
        m = partiallst2.count(k)
        for l in range(m):
            multiset2.append((k, l))
    answer = 1 if multiset1 == [] and multiset2 == [] else len(set(multiset1) & set(multiset2)) / len(set(multiset1) | set(multiset2))
    return int(answer * 65536)