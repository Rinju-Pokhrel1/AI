import random

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

class GoalBasedAgent:
    def __init__(self, start_pos, goal_pos):
        self.location = start_pos
        self.goal = goal_pos
        self.visited = {start_pos}
        self.knowledge_base = {
            (0, 0): "safe",
            (0, 1): "unknown",
            (0, 2): "unknown",
            (1, 0): "unknown",
            (1, 1): "unknown",
            (1, 2): "unknown"
        }

    def get_neighbors(self, pos):
        x, y = pos
        neighbors = []
        possible_moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for move in possible_moves:
            if 0 <= move[0] < 2 and 0 <= move[1] < 3:
                neighbors.append(move)
        return neighbors

    def is_percept_safe(self, pos):
        """Checks if a location is safe based on the absence of danger signals."""
        percepts = get_percepts(pos)
        return "breeze" not in percepts and "stench" not in percepts and "pit" not in percepts and "glitter" not in percepts and "safe" in percepts

    def act(self, percepts):
        if self.location == self.goal and "glitter" in percepts:
            print(f"Goal achieved! Location: {self.location}. Action: Grab Gold!")
            return "Grab Gold"

        if "breeze" in percepts or "stench" in percepts:
            print(f"Percept: Danger near {self.location}. Updating knowledge and retreating.")
            self.knowledge_base[self.location] = "dangerous"
            
            for neighbor in self.get_neighbors(self.location):
                if self.is_percept_safe(neighbor) and neighbor not in self.visited:
                    self.location = neighbor
                    self.visited.add(self.location)
                    return f"Flee to safe cell {self.location}"
            return "Stall"

        if "glitter" not in percepts:
            print(f"Percept: Nothing of note. Planning a move towards goal {self.goal}.")
            for neighbor in self.get_neighbors(self.location):
                if self.is_percept_safe(neighbor) and neighbor not in self.visited:
                    self.location = neighbor
                    self.visited.add(self.location)
                    return f"Move to {self.location}"
        
        return "Stall"

print("--- Simulating the Goal-Based Agent ---")
start_position = (0, 0)
goal_position = (1, 2)
agent = GoalBasedAgent(start_position, goal_position)

print(f"Agent starts at {agent.location} with goal {agent.goal}\n")

for step in range(1, 5):
    print(f"--- Step {step} ---")
    percepts = get_percepts(agent.location)
    action = agent.act(percepts)
    print(f"Action: {action}\n")
    if action == "Grab Gold":
        print("Goal reached. Simulation ends.")
        break
