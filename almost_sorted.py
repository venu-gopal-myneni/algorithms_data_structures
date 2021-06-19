def almostSorted(arr):
    swapy = swap(arr)
    if swapy[0] == "no":
        print("no")

    if swapy[0] == "yes" and swapy[1] is not None:
        print("yes")
        print("swap {} {}".format(swapy[1]+1, swapy[2]+1))
    if swapy[0] == "yes" and swapy[1] is None:
        print("yes")


def swap(array):
    broke_at = None
    mended_at = None
    broke_ele_before = None
    broke_ele = None
    broke_ele_after = None
    for pos in range(len(array)):
        if pos == len(array)-1 and broke_at is None:
            return ("yes", None, None)
        if pos == len(array)-1 and broke_at is not None:
            if (broke_ele_before <= array[pos] <= broke_ele_after):
                if pos-1 >= 0:
                    if array[pos-1] <= broke_ele:
                        mended_at = pos
            if mended_at is not None:
                return ("yes", broke_at, mended_at)
            else:
                return ("no", broke_at, mended_at)
        if broke_at is None:
            if array[pos] > array[pos+1]:
                broke_at = pos
                broke_ele = array[pos]
                if pos-1 >= 0:
                    broke_ele_before = array[pos-1]
                else:
                    broke_ele_before = float("-inf")
                broke_ele_after = array[pos+1]

        elif broke_ele is not None:
            if (broke_ele_before <= array[pos] <= broke_ele_after):
                if pos-1 >= 0:
                    if array[pos-1] <= broke_ele <= array[pos+1]:
                        mended_at = pos
                else:
                    if broke_ele <= array[pos+1]:
                        mended_at = pos
    if broke_at is None:
        return ("yes", None, None)
    if broke_at is not None and mended_at is not None:
        return ("yes", broke_at, mended_at)
    if broke_at is not None and mended_at is None:
        return ("no", broke_at, mended_at)


if __name__ == "__main__":
    arrays = [[2, 3, 5, 4], [1, 2, 3, 4, 10, 6, 7, 8, 9, 5, 20], [1, 2, 3]]
    for array in arrays:
        print(array)
        print(swap(array))
        print("_________________________________________")
