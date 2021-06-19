import bisect
import networkx as nx
import matplotlib.pyplot as plt


def minSwaps_inc_sort(arr):
    # increasing sort
    edges_list = []
    for i, val in enumerate(arr):
        if i != val:
            edges_list.append([val, arr[val]])

    graph = nx.DiGraph()
    graph.add_nodes_from(arr)
    graph.add_edges_from(edges_list)

    cyc_list = list(nx.simple_cycles(graph))
    swaps = 0
    for cyc in cyc_list:
        swaps += len(cyc)-1
    return swaps

    #nx.draw(graph, with_labels=True)
    # plt.show()


def minSwaps_dec_sort(arr):
    # increasing sort
    edges_list = []
    for i, val in enumerate(arr):
        if len(arr)-1-i != val:
            edges_list.append([val, arr[-val-1]])

    graph = nx.DiGraph()
    graph.add_nodes_from(arr)
    graph.add_edges_from(edges_list)

    cyc_list = list(nx.simple_cycles(graph))
    #nx.draw(graph, with_labels=True)
    # plt.show()
    swaps = 0
    for cyc in cyc_list:
        swaps += len(cyc)-1
    return swaps


def lilysHomework(arr):
    barr = sorted(arr)
    carr = []
    for ele in arr:
        pos = bisect.bisect_left(barr, ele)
        if pos not in carr:
            carr.append(pos)
        else:
            while pos in carr:
                pos += 1
            carr.append(pos)

    incre = minSwaps_inc_sort(arr)
    decre = minSwaps_dec_sort(arr)
    return min(incre, decre)


if __name__ == "__main__":
    array = [3, 4, 2, 5, 1]
    # print(lilysHomework(array))
    barray = [i-1 for i in array]
    print(minSwaps_inc_sort(barray))
    print(minSwaps_dec_sort(barray))
