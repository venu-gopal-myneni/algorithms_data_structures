def rect_big_subplot(length, breadth):
    ## strategy : divide & conquer . ANS = GCD of length & beadth
    # base case
    if length % breadth ==0:
        return breadth
    # dividing (logic of Euclidean GCD algorithm )
    else:
        new_breadth = length % breadth
        new_length = breadth
        return rect_big_subplot(new_length, new_breadth)

if __name__ =="__main__":
    A=[[100,50],[120,50],[168,64]]
    for l,b in A:
        print(rect_big_subplot(l, b))