def solution(my_string):
    vowel, answer = 'aeiou', ''
    for i in my_string:
        if i not in vowel:
            answer += i
    return answer