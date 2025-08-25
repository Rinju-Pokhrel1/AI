world = {
    (0, 0): ["safe"],
    (0, 1): ["breeze"],
    (0, 2): ["pit"],
    (1, 0): ["stench"],
    (1, 1): ["safe"],
    (1, 2): ["glitter"]
}

def get_percepts(pos):
    return world.get(pos, [])

class ModelBasedReflexAgent:
    def __init__(self, start_pos):
        self.location = start_pos
        self.visited = {start_pos}
        self.knowledge_base = {start_pos: get_percepts(start_pos)}

    def get_neighbors(self, pos):
        x, y = pos
        neighbors = []
        possible_moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for move in possible_moves:
            if 0 <= move[0] < 2 and 0 <= move[1] < 3:
                neighbors.append(move)
        return neighbors

    def is_safe(self, pos):
        percepts = self.knowledge_base.get(pos, [])
        return "breeze" not in percepts and "stench" not in percepts and "pit" not in percepts

    def act(self, percepts):
        self.knowledge_base[self.location] = percepts
        if "glitter" in percepts:
            print(f"Percept: Glitter at {self.location}. Action: Grab Gold!")
            return "Grab Gold"
        for neighbor in self.get_neighbors(self.location):
            if neighbor not in self.visited and self.is_safe(neighbor):
                self.location = neighbor
                self.visited.add(self.location)
                print(f"Percept: Safe neighbor found. Moving to {self.location}.")
                return f"Move to {self.location}"
        print(f"Percept: No safe unvisited neighbors. Stall at {self.location}.")
        return "Stall"

print("--- Simulating the Model-Based Reflex Agent ---")
start_position = (0, 0)
agent = ModelBasedReflexAgent(start_position)

for step in range(1, 6):
    print(f"--- Step {step} ---")
    percepts = get_percepts(agent.location)
    action = agent.act(percepts)
    print(f"Action: {action}\n")
    if action == "Grab Gold":
        print("Goal reached. Simulation ends.")
        break
