

def solution(A):
    # write your code in Python 3.6
    previous_list = []
    total_count = 0
    for i in range(len(A)):
        if A[i] not in previous_list:
            if len(previous_list) == 1:
                previous_list.append(A[i])
            elif  len(previous_list) == 0:
                previous_list = []
                previous_list.append(A[i])
            else:
                total_count = total_count +1
                previous_list = []
                previous_list.append(A[i])
        else:
            previous_list.append(A[i])
            if len(previous_list) == len(A):
                total_count = total_count +1
    return total_count

A = [2,2,3,4,3,3,2,2,1,1,2,5]
count = solution(A)
print(count)
