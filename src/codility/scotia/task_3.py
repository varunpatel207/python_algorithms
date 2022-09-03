
def solution(S):
    chars = "BANANA"

    remove_count = 0
    is_true = True
    while is_true:
        for char in chars:
            if char in S:
                S = S.replace(char, "", 1)
            else:
                is_true = False
                break
        if is_true:
            remove_count += 1

    return remove_count

s = solution("QABAAAWOBL")
