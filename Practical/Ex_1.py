from collections import deque

def build_path(meet, parent_f, parent_b):
    path = []
    n = meet
    while n is not None:
        path.append(n)
        n = parent_f[n]
    path.reverse()
    n = parent_b[meet]
    while n is not None:
        path.append(n)
        n = parent_b[n]
    return path

def bidirectional_search(graph, source, goal):
    if source == goal:
        return [source]
    parent_f = {source: None}
    parent_b = {goal: None}
    q_f = deque([source])
    q_b = deque([goal])
    while q_f and q_b:
        node = q_f.popleft()
        for nb in graph[node]:
            if nb not in parent_f:
                parent_f[nb] = node
                q_f.append(nb)
                if nb in parent_b:
                    return build_path(nb, parent_f, parent_b)
        node = q_b.popleft()
        for nb in graph[node]:
            if nb not in parent_b:
                parent_b[nb] = node
                q_b.append(nb)
                if nb in parent_f:
                    return build_path(nb, parent_f, parent_b)
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E', 'G'],
    'G': ['F']
}

source, goal = 'A', 'G'
path = bidirectional_search(graph, source, goal)
if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path exists between", source, "and", goal)
