def solution(my_string):
    upperdic = {chr(i) : my_string.count(chr(i)) for i in range(65, 91)}
    lowerdic = {chr(j) : my_string.count(chr(j)) for j in range(97, 123)}
    return list(upperdic.values()) + list(lowerdic.values())