import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def misplaced(state):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != GOAL[i])

def neighbors(state):
    i = state.index(0)
    r, c = divmod(i, 3)
    result = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            s = list(state)
            s[i], s[j] = s[j], s[i]
            result.append(tuple(s))
    return result

def best_first_search(start):
    heap = [(misplaced(start), 0, start)]
    parent = {start: None}
    count = 1
    while heap:
        h, _, state = heapq.heappop(heap)
        if state == GOAL:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]
        for nb in neighbors(state):
            if nb not in parent:
                parent[nb] = state
                heapq.heappush(heap, (misplaced(nb), count, nb))
                count += 1
    return None

def show(state):
    for r in range(3):
        print(*[x if x != 0 else '_' for x in state[r*3:r*3+3]])
    print()

start = (1, 2, 3, 0, 4, 6, 7, 5, 8)
print("Start state:")
show(start)
path = best_first_search(start)
if path:
    print("Solved in", len(path) - 1, "moves\n")
    for step, s in enumerate(path):
        print("Step", step, "(misplaced tiles =", misplaced(s), ")")
        show(s)
else:
    print("No solution")
