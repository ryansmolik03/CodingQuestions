#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    # length of array
    n = len(a)
    # create an array to return
    result = []

    # for each index in the array
    for i in range(n):
        # calculate the new index
        index = (i + d) % n
        # append the new index value to the result array
        result.append(a[index])
    
    # return the result array
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
