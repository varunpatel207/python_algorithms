#!/bin/python3

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sorted_array = sorted(arr)
    minimum_sum = 0
    maximum_sum = 0

    for number in sorted_array[:4]:
        minimum_sum += number

    for number in sorted_array[1:]:
        maximum_sum += number

    print(minimum_sum, maximum_sum)

if __name__ == '__main__':

    # arr = list(map(int, input().rstrip().split()))

    miniMaxSum([1,2,3,4,5])
