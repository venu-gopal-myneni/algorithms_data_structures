import math
def unimodal_search(alist):
    mid = math.floor(len(alist)/2)
    print(mid)
    if ((alist[mid +1] <= alist[mid]) and (alist[mid-1] <= alist[mid])):
        return mid, alist[mid]
    elif ((alist[mid +1] >= alist[mid]) and (alist[mid-1] <= alist[mid])):
        return unimodal_search(alist[mid:])
    else:
        return unimodal_search(alist[0:mid])

if __name__ == "__main__":
    alist=[1,5,6,2,0]
    print(unimodal_search(alist))
