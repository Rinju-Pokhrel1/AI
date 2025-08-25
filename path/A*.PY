import heapq

# Graph: adjacency list with costs
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'C': 4, 'D': 2},
    'B': {'D': 5, 'E': 12},
    'C': {'G': 3},
    'D': {'G': 2},
    'E': {'G': 1},
    'G': {}
}

# Heuristic values (straight-line distance to goal)
heuristic = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'D': 0,
    'E': 1,
    'G': 0
}

class Node:
    def __init__(self, state, parent=None, g=0):
        self.state = state
        self.parent = parent
        self.g = g  # path cost so far

    def path(self):
        node = self
        p = []
        while node:
            p.append(node.state)
            node = node.parent
        return list(reversed(p))

def a_star_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], Node(start, None, 0)))
    visited = {}

    while open_list:
        f, node = heapq.heappop(open_list)
        if node.state == goal:
            return node.path(), node.g
        if node.state in visited and visited[node.state] <= node.g:
            continue
        visited[node.state] = node.g

        for neighbor, cost in graph[node.state].items():
            g = node.g + cost
            f = g + heuristic[neighbor]
            heapq.heappush(open_list, (f, Node(neighbor, node, g)))

    return None, None

# MAIN
start = 'S'
goal = 'G'
solution, cost = a_star_search(start, goal)

if solution:
    print("Path found using A* Search:")
    print(" -> ".join(solution))
    print("Total cost:", cost)
else:
    print("No path found.")
