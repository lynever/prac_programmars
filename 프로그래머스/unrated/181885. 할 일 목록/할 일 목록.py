def solution(todo_list, finished):
    return [todo_list[i] for i in range(0, len(todo_list)) if finished[i] == False]