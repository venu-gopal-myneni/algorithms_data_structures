def gridlandMetro(n, m, k, track):
    # Write your code here
    adict = {}

    total_ava = n*m
    for alist in track:

        if alist[0]-1 not in adict:
            adict[alist[0]-1] = {"used": 0}
        for i in range(alist[1]-1, alist[2]):
            if i not in adict[alist[0]-1]:
                adict[alist[0]-1][i] = 1
                adict[alist[0]-1]["used"] += 1
    used = 0
    for i in adict:
        used += adict[i]["used"]
    return total_ava-used
