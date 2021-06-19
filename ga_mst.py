import networkx as nx

graph = nx.Graph()
edges_list =[("a","b",6),
            ("a","c",12),
            ("b","c",5),
            ("d","b",14),
            ("e","b",8),
            ("d","e",3),
            ("e","f",10),
            ("c","f",7),
            ("c","g",9),
            ("f","h",15)]
graph.add_weighted_edges_from(edges_list)
for i in nx.algorithms.tree.mst.minimum_spanning_edges(graph):
    print(i)