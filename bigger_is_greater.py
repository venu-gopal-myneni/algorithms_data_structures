# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

def biggerIsGreater(w):
    if len(w) == 1:
        return "no answer"
    elif len(w) == 2:
        if w[0] == w[1]:
            return "no answer"
        if w[1] + w[0] > w:
            return w[1]+w[0]
        else:
            return "no answer"
    else:
        alist = list(w)
        rank_dict = {ele: pos for pos, ele in enumerate(sorted(alist))}
        cur_order = [rank_dict[ele] for ele in alist]
        pivot_pos = get_pivot_pos(cur_order)
        if pivot_pos is None:
            return "no answer"
        else:
            succ_pos = right_most_successor_pos(pivot_pos, cur_order)
            alist[pivot_pos], alist[succ_pos] = alist[succ_pos], alist[pivot_pos]
            reversed_list = reversed(alist[pivot_pos+1:])
            # print(list(reversed_list))
            return "".join(alist[0:pivot_pos+1]+list(reversed_list))


def get_pivot_pos(cur_order):
    pivot_pos = None
    for pos in range(1, len(cur_order)):
        if cur_order[pos] > cur_order[pos-1]:
            pivot_pos = pos-1
    return pivot_pos


def right_most_successor_pos(pivot_pos, cur_order):
    for i in range(1, len(cur_order)-pivot_pos):
        if cur_order[-i] > cur_order[pivot_pos]:
            return len(cur_order) - i


if __name__ == "__main__":
    #cur_order = [0, 1, 2, 5, 3, 3, 0]
    # print(get_pivot(cur_order))
    a = ["a", "ab", "ba", "aa", "abcd", "dhck", "dkhc"]
    for i in a:
        print(biggerIsGreater(i))
