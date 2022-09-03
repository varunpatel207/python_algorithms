# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    sorted_a = sorted(set(A))

    has_positive = False
    for index, number in enumerate(sorted_a[:len(sorted_a) - 1]):
        if number > 0:
            if number + 1 != sorted_a[index + 1]:
                return number + 1
            has_positive = True

    if has_positive:
        return sorted_a[-1] + 1
    return 1

A = [-1, -3]
return_value = solution(A)
