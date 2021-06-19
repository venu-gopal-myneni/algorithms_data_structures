def maxSubarray(arr):
    # Write your code here
    # max sub-seq
    seq_sum = max_sub_seq(arr)
    arr_sum = kadane(arr)
    return f"{arr_sum} {seq_sum}"


def max_sub_arr(arr):
    insearch = 0
    sum_list = []
    sumy = 0
    pos = 0

    for pos in range(0, len(arr)):
        if arr[pos] >= 0:
            if insearch == 0:
                sumy += arr[pos]
                insearch = 1
            else:
                sumy += arr[pos]
        else:
            if insearch == 1:
                benefit_sumy = arr[pos]
                starter = pos+1
                blist = [benefit_sumy]
                while starter < len(arr):
                    benefit_sumy += arr[starter]
                    blist.append(benefit_sumy)
                    starter += 1
                maxy = max(blist)
                if maxy > 0:
                    sumy += maxy
                    sum_list.append(sumy)
                    sumy = 0
                    insearch = 0

                else:
                    sum_list.append(sumy)
                    sumy = 0
                    insearch = 0
    sum_list.append(sumy)
    return max(sum_list)


def max_sub_arr2(arr):
    insearch = 0
    sum_list = []
    sumy = 0
    pos = 0
    restart = None
    while pos < len(arr) or restart is None:
        if pos >= len(arr) and restart is not None:
            pos = restart
            restart = None
        if arr[pos] >= 0:
            if insearch == 0:
                sumy += arr[pos]
                insearch = 1
                pos += 1
            else:
                sumy += arr[pos]
                pos += 1
        else:
            if insearch == 1:
                benefit_sumy = arr[pos]
                starter = pos+1
                restart = pos

                while (benefit_sumy <= 0) and (starter < len(arr)):
                    benefit_sumy += arr[starter]
                    starter += 1

                if benefit_sumy > 0:
                    sumy += benefit_sumy
                    pos = starter-1
                else:
                    sum_list.append(sumy)
                    sumy = 0
                    insearch = 0
                    pos += 1
    sum_list.append(sumy)
    return max(sum_list)


def max_sub_seq(arr):
    all_neg = True
    sumy = 0
    for i in arr:
        if i >= 0:
            all_neg = False
            sumy += i
    if all_neg:
        return max(arr)
    return sumy


def kadane(arr):
    all_neg = True
    max_so_far = 0
    max_ending_here = 0
    for i in arr:
        if i > 0:
            all_neg = False
        max_ending_here += i
        if max_ending_here < 0:
            max_ending_here = 0
        else:
            max_so_far = max(max_so_far, max_ending_here)
    if all_neg:
        return max(arr)
    return max_so_far


if __name__ == "__main__":
    alist = [-10]
    print(maxSubarray(alist))
