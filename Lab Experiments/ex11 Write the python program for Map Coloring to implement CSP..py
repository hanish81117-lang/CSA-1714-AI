# Map Coloring Problem using CSP and Backtracking

# Define the map as a graph
map_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Dictionary to store color assignments
color_assignment = {}


# Check whether a color is valid
def is_valid(region, color):
    for neighbor in map_graph[region]:
        if color_assignment.get(neighbor) == color:
            return False
    return True


# Backtracking function
def solve_csp():
    # If all regions are colored, return True
    if len(color_assignment) == len(map_graph):
        return True

    # Select an uncolored region
    region = next(
        r for r in map_graph if r not in color_assignment
    )

    # Try each available color
    for color in colors:
        if is_valid(region, color):
            color_assignment[region] = color

            # Recursively color the remaining regions
            if solve_csp():
                return True

            # Backtrack if no solution is found
            del color_assignment[region]

    return False


# Main program
if solve_csp():
    print("Map Coloring Solution:")
    for region, color in color_assignment.items():
        print(region, ":", color)
else:
    print("No solution exists.")
