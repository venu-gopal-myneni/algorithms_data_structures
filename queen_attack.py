def binary_search(arr, x, pos):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid][pos] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid][pos] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


def bin_search_multi_pos(row_ord_list, rq, pos):
    out_list = []
    first_pos = binary_search(row_ord_list, rq, pos)
    while first_pos != -1:
        out_list.append(first_pos)
        if first_pos < len(row_ord_list):
            first_pos = binary_search(row_ord_list[first_pos+1:], rq, pos)
        else:
            first_pos = -1
    return out_list


def hor_mov(rq, cq, row_ord_list, n):
    # find rows with rq
    first_pos = binary_search(row_ord_list, rq, 0)
    tot_avai = n-1
    while first_pos != -1:
        if first_pos < rq:
            tot_avai = 0


if __name__ == "__main__":
    array = [[0, 2], [1, 2], [1, 4]]
    element = 1
    print(bin_search_multi_pos(array, element, 0))
