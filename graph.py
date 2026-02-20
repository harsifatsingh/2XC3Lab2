from collections import deque
import random

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

#Use the methods below to determine minimum vertex covers

def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.number_of_nodes())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


def BFS2(G, node1, node2):
    if node1 == node2:
        return [node1]
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False

    paths_dict = {}

    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                paths_dict[node] = current_node

                if node == node2:
                    path = [node2]
                    while path[-1] != node1:
                        path.append(paths_dict[path[-1]])
                
                    return path[::-1]
    return []


def DFS2(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False

    paths_dict = {}

    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True

            if current_node == node2:
                path = [node2]
                while path[-1] != node1:
                    path.append(paths_dict[path[-1]])
                path.reverse()
                return path

            for node in G.adj[current_node]:
                if not marked[node]:
                    if node not in paths_dict:
                        paths_dict[node] = current_node
                    S.append(node)

    return []

def BFS3(G, node1):
    Q = deque([node1])

    marked = {}
    for node in G.adj:
        marked[node] = False
    marked[node1] = True

    pred = {}
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                marked[node] = True
                pred[node] = current_node
                Q.append(node)

    return pred


def DFS3(G, node1):
    S = [node1]

    marked = {}
    for node in G.adj:
        marked[node] = False

    pred = {}

    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if not marked[node]:
                    if node not in pred:
                        pred[node] = current_node
                    S.append(node)

    return pred

def has_cycle(G):
    visited = set()
    parent = {}

    for start in G.adj:
        if start in visited:
            continue

        parent[start] = None
        stack = [start]

        while len(stack) != 0:
            v = stack.pop()

            if v not in visited:
                visited.add(v)

                for nbr in G.adj[v]:
                    if nbr not in visited:
                        parent[nbr] = v
                        stack.append(nbr)
                    else:
                        if parent[v] != nbr:
                            return True

    return False


def is_connected(G):
    node1 = list(G.adj.keys())[0]
    for node2 in G.adj:
        if DFS(G, node1, node2) == False:
            return False
    return True

def random_add_edge(G, i):
    node1 = random.randint(0, (i - 1))
    node2 = random.randint(0, (i - 1))

    while (node1 == node2) or (G.are_connected(node1, node2) == True):
        node1 = random.randint(0, (i - 1))
        node2 = random.randint(0, (i - 1))
    
    G.add_edge(node1,node2)


def create_random_graph(i, j):
    G = Graph(i)

    for _ in range(j):
        random_add_edge(G, i)
    
    return G
