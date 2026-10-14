
import heapq

def astar(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            print("Shortest Path:", " -> ".join(path))
            print("Total Cost:", g)
            return

        if node in visited:
            continue
        visited.add(node)

        for neighbour, cost in graph[node].items():
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]
                heapq.heappush(
                    pq, (new_f, new_g, neighbour,
                         path + [neighbour])
                )

    print("No path found")

# Graph with edge costs
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'E': 1},
    'D': {'G': 5},
    'E': {'G': 3},
    'G': {}
}

# Heuristic values to goal G
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'G': 0
}

astar(graph, heuristic, 'A', 'G')
