#!/bin/python3


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_to_right = 0
    right_to_left = 0

    for index in range(len(arr)):
        left_to_right += arr[index][index]
        right_to_left += arr[index][(len(arr) - 1) - index]

    return abs(left_to_right - right_to_left)

if __name__ == '__main__':
    arr = [[1,2,3], [4,5,6], [9,8,9]]
    result = diagonalDifference(arr)

