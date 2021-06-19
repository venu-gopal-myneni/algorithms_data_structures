
def fnbsn(checked_nodes,weights):
    miny = float("inf")
    nbsn =None
    for node,weight in weights.items():
        if node not in checked_nodes:
            if weight < miny:
                nbsn = node
                miny = weight
    return nbsn


def diks(graph,from_node,to_node):
    #parents
    parents={}
    # initialise weights
    weights ={}
    for node in graph:# for node in nodes
        if node == from_node:
            weights[node] =0
        else:
            weights[node] =float("inf")
    weights["F"] =float("inf")
    
    next_best_node = from_node
    parents[from_node] = None
    checked_nodes =[]
    # updating weights from next best node
    while len(checked_nodes)+1 < 6: # total nodes
        if next_best_node in graph:
            for child in graph[next_best_node]:
                if weights[child[0]] > weights[next_best_node] + child[1]:
                    weights[child[0]] =weights[next_best_node] + child[1]
                    parents[child[0]] = next_best_node
        checked_nodes.append(next_best_node)
        print(checked_nodes)
        # finding next best node
        next_best_node =fnbsn(checked_nodes,weights)
    return weights, parents


if __name__ == "__main__":
    graph={}
    graph["S"] =[["A",5], ["B",2]]
    graph["A"] =[["C",4],["D",2]]
    graph["B"] =[["A",8],["D",7]]
    graph["C"] =[["D",6],["F",3]]
    graph["D"] =[["F",1]]
    from_node ="S"
    to_node="F"
    print(diks(graph,from_node,to_node))