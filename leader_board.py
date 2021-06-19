def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


def search_between(array, key, add=0):
    #print(array, key, add)
    if len(array) == 1:
        if array[0] < key:
            return 1+add
        else:
            return 2+add
    mid = len(array)//2
    # print(mid)
    if array[mid] < key < array[mid-1]:
        return mid+1+add
    elif array[mid-1] < key and array[mid] < key:
        return search_between(array[0:mid], key, add)
    else:
        return search_between(array[mid:], key, add+mid)


def climbingLeaderboard(ranked, player):
    same_ranks = {}
    # Write your code here
    player_rank_list = []
    adict = {}
    for i in ranked:
        if i in adict:
            adict[i] += 1
        else:
            adict[i] = 1
    rank = 1
    sorted_keys = list(adict.keys())
    for key in sorted_keys:
        same_ranks[key] = rank
        rank += 1
    # print(adict)
    # print(same_ranks)

    for j in player:
        # print(player_rank_list)
        if (j in adict):
            player_rank_list.append(same_ranks[j])
        else:
            player_rank_list.append(search_between(sorted_keys, j))
    return player_rank_list


if __name__ == "__main__":
    ranked = [100, 90, 90, 80]
    player = [70, 80, 105]
    print(climbingLeaderboard(ranked, player))

    array = [110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    #array = [10, 20]
    key = 55
    print(search_between(array, key, 0))

'''

import math
import os
import random
import re
import sys
import time

def timeit(func):
    def timed(*args, **kw):
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()

        print('%r  %2.2f ms' % (func.__name__, (te - ts) * 1000))
        return result
    return timed
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1

@timeit
def search_between(array, key, add=0):
    #print(array, key, add)
    if len(array) == 1:
        if array[0] < key:
            return 1+add
        else:
            return 2+add
    mid = len(array)//2
    # print(mid)
    if array[mid] < key < array[mid-1]:
        return mid+1+add
    elif array[mid-1] < key and array[mid] < key:
        return search_between(array[0:mid], key, add)
    else:
        return search_between(array[mid:], key, add+mid)

@timeit
def climbingLeaderboard(ranked, player):
    same_ranks = {}
    # Write your code here
    player_rank_list = []
    adict = {}
    sorted_keys=[]
    same_ranks ={}
    rank=1
    for i in ranked:
        if i not in adict:
            adict[i] = 1
            same_ranks[i] = rank
            rank +=1
            sorted_keys.append(i)
    

    for j in player:
        # print(player_rank_list)
        if (j in adict):
            player_rank_list.append(same_ranks[j])
        else:
            player_rank_list.append(search_between(sorted_keys, j))
    return player_rank_list
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
'''
