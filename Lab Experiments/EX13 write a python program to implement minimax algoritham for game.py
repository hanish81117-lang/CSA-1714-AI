

def minimax(depth, node, maximizing, values):
    if depth == 3:
        return values[node]

    if maximizing:
        best = float('-inf')
        for i in range(2):
            score = minimax(depth + 1, node * 2 + i,
                            False, values)
            best = max(best, score)
        print("Maximizing at depth", depth, ":", best)
        return best

    else:
        best = float('inf')
        for i in range(2):
            score = minimax(depth + 1, node * 2 + i,
                            True, values)
            best = min(best, score)
        print("Minimizing at depth", depth, ":", best)
        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

print("Leaf node values:", values)
best_score = minimax(0, 0, True, values)
print("Best score:", best_score)
