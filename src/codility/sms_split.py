

def solution(S, K):
    word_list = S.split()

    message_list = []
    for index, word in enumerate(word_list):
        if message_list:
            if len(word) + len(message_list[-1]) <= K:
                message_list[-1] = " ".join([message_list[-1], word])
            else:
                message_list.append(word)
        else:
            message_list.append(word)

    return len(message_list)

S = "SMS messages are really short"
message_count = solution(S, 12)
print(message_count)
