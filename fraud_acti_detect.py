import bisect


def activityNotifications(expenditure, d):
    first_list = sorted(expenditure[0:d])
    remove_me_pos = 0
    frauds = 0
    if d % 2 == 0:
        medians = (d//2, d//2 - 1)
    else:
        medians = (d//2, d//2)

    for i in expenditure[d:]:
        median = (first_list[medians[0]] + first_list[medians[1]])/2
        del first_list[bisect.bisect_left(
            first_list, expenditure[remove_me_pos])]
        bisect.insort(first_list, i)
        remove_me_pos += 1
        if i >= 2*median:
            frauds += 1
    return frauds


if __name__ == "__main__":

    expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    d = 5
    print(activityNotifications(expenditure, d))
