from collections import deque
from graph import Graph

# Modified breadth first search that returns path from node 1 to node 2
def BFS2(g, node1, node2):
    # Storing both node and path (https://docs.python.org/3/library/collections.html#collections.deque)
    Q = deque([(node1, [node1])])
    marked = {node1: True}
    for node in g.adj:
        if node != node1:
            marked[node] = False

    while len(Q) != 0:
        current_node, path = Q.popleft()
        for node in g.adj[current_node]:
            if node == node2:
                return path + [node2]
            if not marked[node]:
                Q.append((node, path + [node]))
                marked[node] = True
    return []

# Modified depth first search that returns path from node 1 to node 2
def DFS2(g, node1, node2):
    S = [(node1, [node1])]
    marked = {}
    for node in g.adj:
        marked[node] = False

    while len(S) != 0:
        current_node, path = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in g.adj[current_node]:
                if node == node2:
                    return path + [node2]
                S.append((node, path + [node]))
    return []



# Modified breadth first search that returns predecessor dicitonary
def BFS3(g, node1):
    Q = deque([node1])
    marked = {node1 : True}
    predDict = {}
    for node in g.adj:
        if node != node1:
            marked[node] = False

    while len(Q) != 0:
        current_node = Q.popleft()
        for node in g.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                predDict[node] = current_node
    return predDict

# Modified depth first search that returns predecessor dicitonary
def DFS3(g, start):
    S = [start]
    pred = {}
    marked = {}

    for node in g.adj:
        marked[node] = False

    while len(S) != 0:
        current_node = S.pop()

        if not marked[current_node]:
            marked[current_node] = True

            for node in g.adj[current_node]:
                if not marked[node]:
                    S.append(node)
                    if node not in pred:
                        pred[node] = current_node
    return pred

def main():
    g = Graph(5)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,4)
    g.add_edge(2,3)
    g.add_edge(3,4)
    
    print(BFS2(g, 0, 4))
    print(DFS2(g, 0, 4))

    g = Graph(7)
    g.add_edge(1,2)
    g.add_edge(2,4)
    g.add_edge(4,6)
    g.add_edge(1,3)
    g.add_edge(3,4)
    g.add_edge(3,5)
    g.add_edge(5,4)

    print(BFS3(g, 1))
    print(DFS3(g, 1))
    
main()