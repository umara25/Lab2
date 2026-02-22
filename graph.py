from collections import deque
import random

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

    def get_size(self):
        return len(self.adj)


def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1: True}
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


# Umar: returns the path from node1 to node2 as a list of nodes using BFS, or an empty list if no path exists
def BFS2(G, node1, node2):
    Q = deque([node1])
    marked = {node1: True}
    predecessor = {node1: None}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                predecessor[node] = current_node
            if node == node2:
                path = []
                step = node2
                while step is not None:
                    path.append(step)
                    step = predecessor[step]
                path.reverse()
                return path
    return []


# Yusuf: returns the path from node1 to node2 as a list of nodes using DFS, or an empty list if no path exists
def DFS2(G, node1, node2):
    S = [node1]
    marked = {}
    predecessor = {node1: None}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if not marked[node]:
                    predecessor[node] = current_node
                if node == node2:
                    path = []
                    step = node2
                    while step is not None:
                        path.append(step)
                        step = predecessor[step]
                    path.reverse()
                    return path
                S.append(node)
    return []


# Umar: returns a predecessor dictionary encoding paths from node1 to all reachable nodes using BFS
def BFS3(G, node1):
    Q = deque([node1])
    marked = {node1: True}
    predecessor = {}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                predecessor[node] = current_node
    return predecessor


# Yusuf: returns a predecessor dictionary encoding paths from node1 to all reachable nodes using DFS
def DFS3(G, node1):
    S = [node1]
    marked = {}
    predecessor = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if not marked[node]:
                    predecessor[node] = current_node
                S.append(node)
    return predecessor


# Umar: returns True if graph G contains a cycle, False otherwise
def has_cycle(G):
    visited = {}
    for node in G.adj:
        visited[node] = False

    for start in G.adj:
        if not visited[start]:
            S = [(start, -1)]
            while len(S) != 0:
                current_node, parent = S.pop()
                if visited[current_node]:
                    return True
                visited[current_node] = True
                for node in G.adj[current_node]:
                    if not visited[node]:
                        S.append((node, current_node))
                    elif node != parent:
                        return True
    return False


# Yusuf: returns True if every node in graph G is reachable from every other node, False otherwise
def is_connected(G):
    if len(G.adj) == 0:
        return True
    start = next(iter(G.adj))
    predecessor = BFS3(G, start)
    for node in G.adj:
        if node != start and node not in predecessor:
            return False
    return True


# Umar: returns a graph with i nodes and j randomly assigned unique edges
def create_random_graph(i, j):
    G = Graph(i)
    possible_edges = []
    for u in range(i):
        for v in range(u + 1, i):
            possible_edges.append((u, v))
    if j > len(possible_edges):
        j = len(possible_edges)
    chosen = random.sample(possible_edges, j)
    for u, v in chosen:
        G.add_edge(u, v)
    return G


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
            if not (start in C or end in C):
                return False
    return True


def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


# Yusuf: returns a vertex cover using a greedy approach that always picks the highest degree vertex
def approx1(G):
    adj_copy = {node: list(neighbors) for node, neighbors in G.adj.items()}
    C = []
    while True:
        if is_vertex_cover(G, C):
            return C
        v = max(adj_copy, key=lambda node: len(adj_copy[node]))
        C.append(v)
        for neighbor in adj_copy[v]:
            if v in adj_copy[neighbor]:
                adj_copy[neighbor].remove(v)
        adj_copy[v] = []


# Umar: returns a vertex cover by repeatedly selecting a random vertex not already in the cover
def approx2(G):
    nodes = list(G.adj.keys())
    C = []
    while True:
        if is_vertex_cover(G, C):
            return C
        remaining = [v for v in nodes if v not in C]
        if not remaining:
            return C
        v = random.choice(remaining)
        C.append(v)


# Yusuf: returns a vertex cover by repeatedly selecting a random edge and adding both endpoints
def approx3(G):
    adj_copy = {node: list(neighbors) for node, neighbors in G.adj.items()}
    C = []
    while True:
        if is_vertex_cover(G, C):
            return C
        edges = []
        for u in adj_copy:
            for v in adj_copy[u]:
                if u < v:
                    edges.append((u, v))
        if not edges:
            return C
        u, v = random.choice(edges)
        if u not in C:
            C.append(u)
        if v not in C:
            C.append(v)
        for neighbor in adj_copy[u]:
            if u in adj_copy[neighbor]:
                adj_copy[neighbor].remove(u)
        adj_copy[u] = []
        for neighbor in adj_copy[v]:
            if v in adj_copy[neighbor]:
                adj_copy[neighbor].remove(v)
        adj_copy[v] = []


# Umar: returns the maximum independent set of graph G using brute force
def MIS(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    max_set = []
    for subset in subsets:
        independent = True
        for u in subset:
            for v in subset:
                if u != v and G.are_connected(u, v):
                    independent = False
        if independent and len(subset) > len(max_set):
            max_set = subset
    return max_set
