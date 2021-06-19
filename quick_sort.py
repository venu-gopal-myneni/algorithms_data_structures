import random
import time
import matplotlib.pyplot as plt 
def bubbleSort(arr):
    n = len(arr)
  
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
def quick_sort(alist):
    if len(alist) <=1:
        return alist
    elif len(alist) ==2:
        if alist[0] <= alist[1]:
            return alist
        else:
            return [alist[1],alist[0]]
    elif len(alist) >=3:
        left_list=[]
        right_list=[]
        pivot_point =1
        for i in alist[0:pivot_point]:
            if i <= alist[pivot_point]:
                left_list.append(i)
            else:
                right_list.append(i)
        for i in alist[pivot_point+1:]:
            if i <= alist[pivot_point]:
                left_list.append(i)
            else:
                right_list.append(i)
        return quick_sort(left_list) +[alist[pivot_point]] + quick_sort(right_list)

if __name__ == "__main__":
    time_list=[]
    n_list =[100,1000]
    for j in n_list:
        a=[random.randrange(1, 50000, 1) for i in range(j)]
        start_time = time.time()
        #quick_sort(a)
        bubbleSort(a)
        #sorted(a)
        time_list.append(time.time()-start_time)
    plt.plot(n_list,time_list,marker="*")
    plt.show()
    



        
