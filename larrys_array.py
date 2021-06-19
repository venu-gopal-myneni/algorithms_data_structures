#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.


def larrysArray(A):
    inversion = 0
    previous = [A[0]]
    for i in A[1:]:
        for j in previous:
            if i < j:
                inversion += 1
        previous.append(i)

    if (inversion) % 2 == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
