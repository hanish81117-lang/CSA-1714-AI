
def alpha_beta(depth, node, is_max, scores, alpha, beta):
    if depth == 3:
        return scores[node]

    if is_max:
        best = -9999

        for i in range(2):
            value = alpha_beta(
                depth + 1, node * 2 + i,
                False, scores, alpha, beta
            )
            best = max(best, value)
            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best

    else:
        best = 9999

        for i in range(2):
            value = alpha_beta(
                depth + 1, node * 2 + i,
                True, scores, alpha, beta
            )
            best = min(best, value)
            beta = min(beta, best)

            if alpha >= beta:
                break

        return best


scores = list(map(int, input(
    "Enter 8 leaf node scores separated by spaces: "
).split()))

if len(scores) != 8:
    print("Please enter exactly 8 scores.")
else:
    result = alpha_beta(0, 0, True, scores, -9999, 9999)
    print("Leaf node scores:", scores)
    print("Best value for MAX:", result)
