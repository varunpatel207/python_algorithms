def solution(S, K):
    day_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    if K > 8:
        remaining_day_count = (K % 7)
    else:
        remaining_day_count = K
    current_day = day_list.index(S)
    if remaining_day_count == 0:
        return day_list[current_day]

    while True:
        if current_day == len(day_list) - 1:
            current_day = 0
        else:
            current_day = current_day + 1

        remaining_day_count -= 1
        if remaining_day_count == 0:
            final_day = day_list[current_day]
            break

    return final_day

s = solution("Wed", 2)
print(s)


