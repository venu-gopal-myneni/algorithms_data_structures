from collections import deque


def bfs_path_to(graph, from_node, to_node):
    qu = deque()
    qu.append(from_node)
    found = False
    cur_node = qu[0]
    parent_dict = {}
    parent_dict[cur_node] = None
    while (len(qu) > 0 and found == False):
        cur_node = qu[0]
        for adj_node in graph[cur_node]:
            if adj_node == to_node:
                parent_dict[adj_node] = cur_node
                found = True
                return parent_dict
            else:
                qu.append(adj_node)
                parent_dict[adj_node] = cur_node
        qu.popleft()

    return parent_dict


def find_path(parent_dict, from_node, to_node):
    if to_node in parent_dict:
        path = to_node
        parent = parent_dict[to_node]
        while parent != None:
            path = parent + " --> " + path
            parent = parent_dict[parent]
        return path
    else:
        return None


if __name__ == "__main__":
    graph = {}
    graph["venu"] = ["alice", "bob", "claire"]
    graph['bob'] = ["anuj", "peggy"]
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []

    from_node = 'venu'
    to_node = 'jonny'
    parent_dict = bfs_path_to(graph, from_node, to_node)
    # print(parent_dict)
    print(find_path(parent_dict, from_node, to_node))
