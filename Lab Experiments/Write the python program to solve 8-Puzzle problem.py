from collections import deque

# Goal state
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Possible movements of the blank tile
MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def solve(start):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        # Check goal
        if state == GOAL:
            return path + [state]

        # Find blank position
        blank = state.index(0)

        # Generate next states
        for move in MOVES[blank]:
            new_state = list(state)
            new_state[blank], new_state[move] = \
                new_state[move], new_state[blank]

            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))

    return None


# Input puzzle
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

# Solve the puzzle
solution = solve(start)

# Display solution
if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)
    print()

    for step, state in enumerate(solution):
        print("Step", step)
        print_puzzle(state)
else:
    print("No solution found.")
