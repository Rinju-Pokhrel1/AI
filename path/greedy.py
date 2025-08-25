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
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def path(self):
        node = self
        p = []
        while node:
            p.append(node.state)
            node = node.parent
        return list(reversed(p))

def best_first_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], Node(start)))
    visited = set()

    while open_list:
        _, node = heapq.heappop(open_list)
        if node.state == goal:
            return node.path()
        visited.add(node.state)
        for neighbor in graph[node.state]:
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristic[neighbor], Node(neighbor, node)))
    return None

# MAIN
start = 'S'
goal = 'G'
solution = best_first_search(start, goal)

if solution:
    print("Path found using Best-First Search:")
    print(" -> ".join(solution))
else:
    print("No path found.")
