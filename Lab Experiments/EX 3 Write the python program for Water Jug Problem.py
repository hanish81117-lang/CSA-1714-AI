
from collections import deque

def water_jug(capacity1, capacity2, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        jug1, jug2 = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        print("Jug 1:", jug1, "Jug 2:", jug2)

        if jug1 == target or jug2 == target:
            print("Target amount reached!")
            return

        states = [
            (capacity1, jug2),  # Fill Jug 1
            (jug1, capacity2),  # Fill Jug 2
            (0, jug2),          # Empty Jug 1
            (jug1, 0),          # Empty Jug 2
            # Pour Jug 1 into Jug 2
            (jug1 - min(jug1, capacity2 - jug2),
             jug2 + min(jug1, capacity2 - jug2)),
            # Pour Jug 2 into Jug 1
            (jug1 + min(jug2, capacity1 - jug1),
             jug2 - min(jug2, capacity1 - jug1))
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("Target amount cannot be reached.")

# Jug capacities and target amount
water_jug(4, 3, 2)
