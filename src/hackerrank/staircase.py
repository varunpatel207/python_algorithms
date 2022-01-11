#!/bin/python3

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for occ in range(1, n+1):
        print(" " * (n - occ) + "#" * occ)

if __name__ == '__main__':
    staircase(4)
