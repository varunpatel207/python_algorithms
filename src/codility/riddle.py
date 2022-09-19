
def solution(riddle):
    alphabet = []
    for i in range(97, 123):
        alphabet.append(chr(i))

    if len(riddle) > 1:
        for index, letter in enumerate(riddle):
            if letter == "?":
                if index >= 1 and index < len(riddle) - 1:
                    new_letter = [item for item in alphabet if item not in [riddle[index - 1], riddle[index + 1]]][0]
                elif index == 0:
                    new_letter = [item for item in alphabet if item not in [riddle[index + 1]]][0]
                elif index == len(riddle) - 1:
                    new_letter = [item for item in alphabet if item not in [riddle[index - 1]]][0]
                riddle = riddle[:index] + new_letter + riddle[index + 1:]
    else:
        if riddle == "?":
            riddle = alphabet[0]

    return riddle
riddle = "???????"
sol = solution(riddle)
print(sol)