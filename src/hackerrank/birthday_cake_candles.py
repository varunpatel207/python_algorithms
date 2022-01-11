#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max_candle = max(candles)
    return candles.count(max_candle)

if __name__ == '__main__':
    result = birthdayCakeCandles([4,4,4,1,3])
    print(result)

